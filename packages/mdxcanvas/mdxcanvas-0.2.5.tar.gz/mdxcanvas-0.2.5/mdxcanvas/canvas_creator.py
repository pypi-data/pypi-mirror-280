import json
import random
import sys
import textwrap
import uuid
from datetime import datetime

import pytz
from canvasapi import Canvas
from canvasapi.assignment import Assignment
from canvasapi.course import Course
from canvasapi.module import Module
from canvasapi.folder import Folder
from canvasapi.quiz import Quiz

import markdown as md
import re

from pathlib import Path
from bs4 import BeautifulSoup, Tag

from markdown.extensions.codehilite import makeExtension as makeCodehiliteExtension

from zipfile import ZipFile, ZipInfo

from .jinja_parser import process_jinja
from .extensions import BlackInlineCodeExtension, CustomTagExtension, BakedCSSExtension
from .parser import DocumentParser, make_iso, Parser
from .yaml_parser import DocumentWalker, parse_yaml


def print_red(string):
    print(string, file=sys.stderr)


# Check if pygments is installed
try:
    from pygments.formatters import HtmlFormatter
except ImportError:
    print_red("Pygments is not installed. Syntax highlighting is not enabled.")


def readfile(filepath: Path):
    with open(filepath) as file:
        return file.read()


def upload_file(folder: Folder, file_path: Path):
    """
    Uploads a file to Canvas, and returns the id of the uploaded file.
    """
    print(f"Uploading {file_path.name} ... ", end="")
    file_id = folder.upload(file_path)[1]["id"]
    return file_id


def create_file_tag(course: Course, canvas_folder: Folder, file_path: Path, display_text: str) -> Tag:
    """
    Returns a tag that links to a file in Canvas.
    """
    file_id = upload_file(canvas_folder, file_path)
    a = Tag(name="a")
    a["href"] = f"/courses/{course.id}/files/{file_id}/preview"
    a.append(display_text)
    return a


def link_file(course: Course, canvas_folder: Folder, parent_folder: Path, tag: Tag) -> Tag:
    """
    Returns a modified tag that links to a file in Canvas.
    Syntax: <file path="./resources/websters.txt" name="dictionary.txt" />Download File</file>
    Alternate: <file path="./resources/file.txt" />
    The alternate syntax uses the last part of the path as the file name, and the file name as the display text.
    """
    file_path = parent_folder / tag.get("path")
    file_name = tag.get("name") or file_path.name
    display_text = tag.text if tag.text.strip() else file_name
    return create_file_tag(course, canvas_folder, file_path, display_text)


def link_zip_tag(course: Course, canvas_folder: Folder, parent_folder: Path, tag: Tag) -> Tag:
    """
    Zips a folder and uploads it to Canvas.
    Syntax: <zip
                path="./resources/solution"
                name="progresscheck1.zip"
                priority_path="./resources/assignment"
                exclude="*.jpg|*.png"
            >
            Download Progress Check 1
            </zip>
    Alternate: <zip path="./resources/progress_check_1" />
    This would use progress_check_1.zip as the name, and "progress_check_1" as the display text.
    """
    folder_name = tag.get("path")
    name = tag.get("name") or f"{folder_name}.zip"
    priority_folder = tag.get("priority_path")
    if priority_folder:
        priority_folder = parent_folder / priority_folder
        if not priority_folder.exists():
            print(f"Priority folder {priority_folder} does not exist, ignoring", file=sys.stderr)
            priority_folder = None
    exclude = tag.get("exclude")
    if exclude:
        exclude = re.compile(exclude)

    folder_path = parent_folder / folder_name
    path_to_zip = parent_folder / name
    display_text = tag.text if tag.text.strip() else name

    print(f"Zipping {folder_path.name} ... ", end="")
    zip_folder(folder_path, path_to_zip, exclude, priority_folder)
    print("Done")
    tag = create_file_tag(course, canvas_folder, path_to_zip, display_text)

    # Then delete the zip
    path_to_zip.unlink()
    return tag


def zip_folder(folder_path: Path, path_to_zip: Path, exclude: re.Pattern = None, priority_fld: Path = None):
    """
    Zips a folder, excluding files that match the exclude pattern.
    Items from the priority folder are added to the zip if they are not in the standard folder.
    Items in the priority folder take precedence over items in the standard folder.
    """
    with ZipFile(path_to_zip, "w") as zipf:
        for item in folder_path.glob("*"):
            write_item_to_zip(item, zipf, exclude, priority_fld=priority_fld)


def write_item_to_zip(item: Path, zipf: ZipFile, exclude: re.Pattern = None, prefix='', priority_fld: Path = None):
    if exclude and exclude.match(item.name):
        print(f"Excluding file {item.name} ... ", end="")
        return
    if item.is_dir():
        write_directory(item, zipf, exclude, prefix, priority_fld / item.name)
    else:
        write_file(item, zipf, prefix, priority_fld)


def write_directory(folder: Path, zipf: ZipFile, exclude: re.Pattern = None, prefix='',
                    priority_fld: Path = None):
    prefix = prefix + folder.name + '/'

    # Get all items in the folder
    paths = list(folder.glob("*"))

    # Add items from priority folder that are not in the folder
    item_names = {i.name for i in folder.glob("*")}
    if priority_fld:
        for item in priority_fld.glob("*"):
            if item.name not in item_names:
                paths.append(item)
                print(f"Using additional file {item.name} .. ", end="")

    for path in paths:
        write_item_to_zip(path, zipf, exclude, prefix, priority_fld)


def set_time_1980(file, prefix=''):
    """
    Ensures that the zip file stays consistent between runs.
    """
    zinfo = ZipInfo(
        prefix + file.name,
        date_time=(1980, 1, 1, 0, 0, 0)
    )
    return zinfo


def write_file(file: Path, zipf: ZipFile, prefix='', priority_fld: Path = None):
    # Use the file from the priority folder if it exists
    if priority_fld and (priority_file := priority_fld / file.name).exists():
        file = priority_file
        print(f"Prioritizing file {file.name} .. ", end="")

    # For consistency, set the time to 1980
    zinfo = set_time_1980(file, prefix)
    try:
        with open(file) as f:
            zipf.writestr(zinfo, f.read())
    except UnicodeDecodeError as _:
        with open(file, 'rb') as f:
            zipf.writestr(zinfo, f.read())


def _parse_slice(field: str) -> slice:
    """
    Parse a 1-based, inclusive slice
    """
    tokens = field.split(':')
    tokens = [
        int(token) if token else None
        for token in tokens
    ]
    if len(tokens) == 1:  # e.g. "3"
        tokens.append(None)

    if tokens[1] is not None:  # e.g. "3:5"
        tokens[1] += 1  # i.e. make it inclusive

    return slice(tokens[0], tokens[1])


def link_include_tag(
        course: Course,
        canvas_folder: Folder,
        parent_folder: Path,
        tag: Tag,
        global_css: str
) -> Tag:
    """
    Replace the `include` tag with the processed HTML of the specified file

    <include path="instructions.md" />
    <include path="demo.py" fenced="true" />
    <include path='demo.py" fenced="true" lines="3:7" />
    lines: 1-based, inclusive bounds
    """
    imported_filename = tag.get('path')
    imported_file = (parent_folder / imported_filename).resolve()
    imported_raw_content = imported_file.read_text()

    lines = tag.get('lines', '')
    if lines:
        grab = _parse_slice(lines)
        imported_raw_content = '\n'.join(imported_raw_content.splitlines()[grab])

    parser = Parser()
    if parser.parse(tag.get('fenced', 'false'), bool):
        imported_raw_content = f'```{imported_file.suffix.lstrip(".")}\n{imported_raw_content}\n```\n'

    imported_html = get_fancy_html(imported_raw_content, course, canvas_folder, imported_file.parent, global_css)

    tag = Tag(name='div')
    tag['data-source'] = imported_filename
    if lines:
        tag['data-lines'] = lines
    tag.extend(BeautifulSoup(imported_html, "html.parser"))
    return tag


def get_fancy_html(markdown_or_file: str, course: Course, canvas_folder: Folder, files_folder: Path, global_css: str = ''):
    """
    Converts markdown to html, and adds syntax highlighting to code blocks.
    """
    if markdown_or_file.endswith('.md'):
        markdown_or_file = readfile(files_folder / markdown_or_file)

    dedented = textwrap.dedent(markdown_or_file)

    fenced = md.markdown(dedented, extensions=[
        'fenced_code',
        'tables',
        'attr_list',

        # This embeds the highlight style directly into the HTML
        # instead of using CSS classes
        makeCodehiliteExtension(noclasses=True),

        # This forces the color of inline code to be black
        # as a workaround for Canvas's super-ugly default red :P
        BlackInlineCodeExtension(),

        CustomTagExtension({
            "file": lambda tag: link_file(course, canvas_folder, files_folder, tag),
            "zip": lambda tag: link_zip_tag(course, canvas_folder, files_folder, tag),
            "include": lambda tag: link_include_tag(course, canvas_folder, files_folder, tag, global_css)
        }),

        BakedCSSExtension(global_css)
    ])
    return fenced


def get_canvas_folder(course: Course, folder_name: str, parent_folder_path="") -> Folder:
    """
    Retrieves an object representing a digital folder in Canvas. If the folder does not exist, it is created.
    """
    folders = list(course.get_folders())
    if not any(fl.name == folder_name for fl in folders):
        print(f"Created {folder_name} folder")
        return course.create_folder(name=folder_name, parent_folder_path=parent_folder_path, hidden=True)
    matches = [fl for fl in folders if fl.name == folder_name]
    return matches[0]


def create_resource_folder(course, quiz_title: str, course_folders):
    """
    Creates a folder in Canvas to store images and other resources.
    """
    generated_folder_name = "Generated-Content"
    if not any(fl.name == generated_folder_name for fl in course_folders):
        print("Created Content Folder")
        course.create_folder(name=generated_folder_name, parent_folder_path="", hidden=True)

    if not any(fl.name == quiz_title for fl in course_folders):
        print(f"Created {quiz_title} folder")
        course.create_folder(name=quiz_title, parent_folder_path=generated_folder_name,
                             hidden=True)


def generate_id(string: str) -> str:
    """
    Deterministic id generator for a given string.
    """
    return str(uuid.UUID(int=random.Random(string).getrandbits(128), version=4))


def get_img_html(image_name, alt_text, style, course, image_folder: Path):
    """
    Returns the html for an image, and the path to the resource, so it can later be uploaded to Canvas.
    After uploading, the correct resource id must be substituted for the fake id using a text replace.
    """
    fake_object_id = generate_id(f"{image_name}{alt_text}{style}")
    style_text = f'style="{style}"' if style else ""
    html_text = f'<p><img id="{image_name}" src="/courses/{course.id}/files/{fake_object_id}/preview" alt="{alt_text}" {style_text}/></p>'
    resource = (fake_object_id, str(image_folder / image_name))
    return html_text, resource


def process_images(html, course: Course, image_folder: Path):
    """
    Finds all the images in the html, and replaces them with html that links to the image in Canvas.
    Returns the new html, and a list of resources that need to be uploaded.
    After uploading, the correct object id must be substituted for the fake ids, which are returned in the resources.
    """
    soup = BeautifulSoup(html, "html.parser")
    matches = soup.find_all('img')
    resources = []
    for img in matches:
        basic_image_html, resource = get_img_html(img["src"], img["alt"], img.get("style"), course, image_folder)
        img.replace_with(BeautifulSoup(basic_image_html, "html.parser"))
        resources.append(resource)
    return str(soup), resources


def process_markdown(markdown_or_file: str, course: Course, canvas_folder: Folder, resource_folder, global_css):
    """
    Converts markdown to html, and adds syntax highlighting to code blocks.
    Then, finds all the images in the html, and replaces them with html that links to the image in Canvas.
    """
    html = get_fancy_html(markdown_or_file, course, canvas_folder, resource_folder, global_css)
    return process_images(html, course, resource_folder)


def get_group_id(course: Course, group_name: str, names_to_ids: dict[str, int]):
    """
    Group ids are numbers that stand for groups like Labs, Projects, etc.
    Since users will provide names for groups, this method is necessary to find ids.
    """
    if not group_name:
        return None

    if group_name not in names_to_ids:
        print("Created Assignment Group: " + group_name)
        course.create_assignment_group(name=group_name)
        for g in course.get_assignment_groups():
            if g.name not in names_to_ids:
                names_to_ids[g.name] = g.id

    return names_to_ids[group_name]


def replace_questions(quiz: Quiz, questions: list[dict]):
    """
    Deletes all questions in a quiz, and replaces them with new questions.
    """
    print(f"Replacing questions ... ", end="")
    for quiz_question in quiz.get_questions():
        quiz_question.delete()
    for question in questions:
        quiz.create_question(question=question)


def get_section_id(course: Course, section_name: str):
    sections = course.get_sections()
    for section in sections:
        if section.name == section_name:
            return section.id
    print(f"Valid section names: {[s.name for s in sections]}")
    return None


def get_page_url(course: Course, page_name: str):
    pages = course.get_pages()
    for page in pages:
        if page.title == page_name:
            return page.url
    print_red(f"Could not find page {page_name}")
    return None


def get_quiz(course: Course, title: str, delete=False):
    return get_canvas_object(course.get_quizzes, "title", title, delete)


def get_assignment(course: Course, assignment_name, delete=False):
    return get_canvas_object(course.get_assignments, "name", assignment_name, delete)


def get_module(course: Course, module_name: str, delete=False):
    return get_canvas_object(course.get_modules, "name", module_name, delete)


def get_canvas_object(course_getter, attr_name, attr, delete=False):
    objects = course_getter()
    for obj in objects:
        if obj.__getattribute__(attr_name) == attr:
            if not delete:
                return obj
            obj.delete()
    return None


def get_override(assignment: Assignment, override_name, delete=False):
    return get_canvas_object(assignment.get_overrides, "title", override_name, delete)


def get_page(course: Course, title, delete=False):
    return get_canvas_object(course.get_pages, "title", title, delete)


def get_module_item(module: Module, item_name, delete=False):
    return get_canvas_object(module.get_module_items, "title", item_name, delete)


def get_object_id_from_element(course: Course, item):
    if item["type"] == "Quiz":
        if not (quiz := get_quiz(course, item["title"])):
            return None
        return quiz.id
    elif item["type"] == "Assignment":
        if not (assignment := get_assignment(course, item["title"])):
            return None
        return assignment.id
    elif item["type"] == "Page":
        page_url = get_page_url(course, item["title"])
        item["page_url"] = page_url


def fix_dates_attribute(element, attribute, time_zone):
    if attribute in element:
        datetime_version = datetime.fromisoformat(make_iso(element[attribute], time_zone))
        utc_version = datetime_version.astimezone(pytz.utc)
        element[attribute] = utc_version.isoformat()


def fix_dates(element, time_zone):
    print(f"Adding time zone to dates ... ", end="")
    fix_dates_attribute(element, "due_at", time_zone)
    fix_dates_attribute(element, "unlock_at", time_zone)
    fix_dates_attribute(element, "lock_at", time_zone)
    fix_dates_attribute(element, "show_correct_answers_at", time_zone)


def modify_assignment(course, element, delete: bool):
    name = element["name"]
    if canvas_assignment := get_assignment(course, name, delete):
        print(f"Editing canvas assignment {name} ...  ", end="")
        canvas_assignment.edit(assignment=element["settings"])
    else:
        print(f"Creating canvas assignment {name} ...  ", end="")
        course.create_assignment(assignment=element["settings"])
    print("Done")
    return canvas_assignment


def modify_quiz(course: Course, element, delete: bool):
    name = element["name"]
    print("Getting quiz from canvas")
    if canvas_quiz := get_quiz(course, name, delete):
        canvas_quiz: Quiz
        print(f"Editing canvas quiz {name} ...  ", end="")
        canvas_quiz.edit(quiz=element)
    else:
        canvas_quiz = create_quiz(course, element, name, element)

    replace_questions(canvas_quiz, element["questions"])
    canvas_quiz.edit()
    print("Done")
    return canvas_quiz


def create_quiz(course, element, name, settings):
    print(f"Creating canvas quiz {name} ...  ", end="")
    try:
        canvas_quiz = course.create_quiz(quiz=element)
    except Exception as ex:
        print(ex)
        print()
        # Perhaps the quiz was partially created, and then the program crashed
        if canvas_quiz := get_quiz(course, name):
            canvas_quiz: Quiz
            print_red("Attempting to edit partially created quiz ...")
            try:
                canvas_quiz.edit(quiz=settings)
            except Exception as ex:
                print_red("Failed to edit quiz")
                raise ex
        else:
            print_red("Quiz was not created")
            print_red("Attempting to debug quiz creation")
            canvas_quiz = debug_quiz_creation(canvas_quiz, course, settings)
    return canvas_quiz


def debug_quiz_creation(canvas_quiz, course, settings):
    new_settings = {"title": settings["title"]}
    keys = list(settings.keys())
    values = list(settings.values())
    for index in range(1, len(settings)):
        new_settings[keys[index]] = values[index]
        print_red(f"Attempting with {keys[index]}: {values[index]}")
        try:
            canvas_quiz = course.create_quiz(quiz=new_settings)
        except Exception as ex:
            print_red(f"Failed on key: {keys[-1]}, value: {values[-1]}")
            raise ex
        canvas_quiz.delete()
    return canvas_quiz


def upload_and_link_files(document_object, course, resources: list[tuple], course_folders):
    """
    Uploads all the files in the resources list, and replaces the fake ids in the document with the real ids.
    """
    print(f"Uploading resources ... ", end="")
    create_resource_folder(course, document_object["name"], course_folders)
    text = json.dumps(document_object, indent=4)
    for fake_id, full_path in resources:
        try:
            resource_id = str(course.upload(full_path)[1]["id"])
            text = text.replace(fake_id, resource_id)
        except IOError:
            print(f"File: {full_path} does not exist, leaving as is")
    return json.loads(text)


def delete_module_item_if_exists(module, name):
    for item in module.get_module_items():
        if item.title == name:
            print(f"Deleting module item {name} ...")
            item.delete()


def create_or_edit_module_item(module: Module, element, object_id, position):
    """
    Creates a module item with an object id, like an assignment or a quiz.
    """
    element["position"] = position
    if not object_id:
        create_or_edit_module_item_without_id(module, element)
    else:
        create_or_edit_module_item_with_id(module, element, object_id)


def create_or_edit_module_item_with_id(module: Module, element, object_id):
    """
    Create module item if it doesn't exist, otherwise edit it.
    """
    element["content_id"] = object_id
    if module_item := get_module_item(module, element["title"]):
        print(f"Editing module item {element['title']} in module {module.name} ...  ", end="")
        module_item.edit(module_item=element)
    else:
        print(f"Creating module item {element['title']} in module {module.name} ...  ", end="")
        module.create_module_item(module_item=element)
    print("Done")


def create_or_edit_module_item_without_id(module: Module, element):
    """
    Creates a module item without an object id, like a page or a header.
    """
    if element["type"] not in ["ExternalUrl", "SubHeader", "Page"]:
        print_red(f"{element['title']} does not exist, no id found when creating module.")
        return

    for item in module.get_module_items():
        if item.title == element["title"]:
            print(f"Editing module item {element['title']} in module {module.name} ...  ", end="")
            item.edit(module_item=element)
            print("Done")
            return

    if element["type"] == "Page" and not element["page_url"]:
        print_red(f"Could not find page url for {element['title']}")
        return

    print(f"Creating module item {element['title']} in module {module.name} ...  ", end="")
    module.create_module_item(module_item=element)
    print("Done")


def delete_module_items_from_element(canvas_module, element):
    names = []
    for item in element["items"]:
        names.append(item["title"])
    for item in canvas_module.get_module_items():
        if item.title not in names:
            print(f"Deleting module item {item.title} ...")
            item.delete()


def create_or_update_module_items(course: Course, element, canvas_module):
    if "items" not in element:
        return
    delete_module_items_from_element(canvas_module, element)
    for index, item in enumerate(element["items"]):
        object_id = get_object_id_from_element(course, item)
        create_or_edit_module_item(canvas_module, item, object_id, index + 1)


def modify_module(course, element):
    name = element["name"]
    if canvas_module := get_module(course, name):
        print(f"Editing canvas module {name} ...  ", end="")
        canvas_module.edit(module=element["settings"])
    else:
        print(f"Creating canvas module {name} ...  ", end="")
        canvas_module = course.create_module(module=element["settings"])
    print()
    create_or_update_module_items(course, element, canvas_module)
    return canvas_module


def get_assignment_override_pairs(course, overrides):
    """
    Searches for canvas assignments with names that match the override names.
    """
    assignments = course.get_assignments()
    pairs = []
    for assignment in assignments:
        for override in overrides:
            if assignment.name == override["title"]:
                pairs.append((assignment, override))
    return pairs


def create_or_update_override_for_assignment(assignment, override, students, sections, section_ids):
    overrides = []
    if students:
        student_override = override.copy()
        student_override["student_ids"] = students
        student_override["title"] = "".join(students)
        overrides.append(student_override)

    for section, s_id in zip(sections, section_ids):
        section_override = override.copy()
        section_override["title"] = section
        section_override["course_section_id"] = s_id
        overrides.append(section_override)

    for override in overrides:
        if canvas_override := get_override(assignment, override["title"]):
            print(f"Editing override {override['title']} ...  ", end="")
            canvas_override.edit(assignment_override=override)
        else:
            print(f"Creating override {override['title']} ...  ", end="")
            assignment.create_override(assignment_override=override)
        print("Done")


def modify_override(course, override, time_zone: str):
    students = override["students"]
    sections = override["sections"]
    section_ids = get_section_ids(course, sections)
    assignment_names = [a['title'] for a in override["assignments"]]

    assignment_override_pairs = get_assignment_override_pairs(course, override["assignments"])
    if not assignment_override_pairs:
        print_red(f"Could not find {assignment_names} in canvas for override {override['sections']}")
        return
    if not students and not sections:
        raise ValueError("Must provide either students or sections")

    for assignment, override in assignment_override_pairs:
        fix_dates(override, time_zone)
        create_or_update_override_for_assignment(assignment, override, students, sections, section_ids)


def get_section_ids(course, names):
    sections = course.get_sections()
    sections = [s.id for s in sections if s.name in names]
    if not sections:
        raise ValueError(f"Could not find sections {sections}")
    return sections


def modify_page(course: Course, element, delete: bool):
    name = element["name"]
    if canvas_page := get_page(course, name, delete):
        print(f"Editing canvas page {name} ...  ", end="")
        canvas_page.edit(wiki_page=element["settings"])
    else:
        print(f"Creating canvas page {name} ...  ", end="")
        canvas_page = course.create_page(wiki_page=element["settings"])
    print("Done")
    return canvas_page


def post_document(course: Course, time_zone,
                  file_path: Path,
                  args_path: Path | None,
                  global_args_path: Path | None,
                  line_id: str | None,
                  css_path: Path | None,
                  delete: bool = False):
    """
    Parses a markdown file, and posts the elements to Canvas.
    :param course: The canvas course to post to, obtained from the canvas api
    :param time_zone: The time zone of the course (e.g. "America/Denver")
    :param file_path: The path to the markdown file
    :param args_path: The path to a csv file containing the template arguments
    :param global_args_path: The path to a csv or json file containing optional global arguments
    :param line_id: One or more argument set id's
    :param css_path: The path to a css file
    :param delete: If true, deletes all elements in the Canvas course with the same name as the elements in the file
    """

    print(f"Parsing file ({file_path.name}) ...  ", end="")

    assignment_groups = list(course.get_assignment_groups())
    names_to_ids = {g.name: g.id for g in assignment_groups}

    if '.jinja' in file_path.name:
        if not args_path:
            raise ValueError("Template arguments must be provided")
        content = process_jinja(file_path, args_path, global_args_path, line_id)
    else:
        content = file_path.read_text()

    print(f"Getting course folders ... ")
    course_folders = list(course.get_folders())
    name_of_file = file_path.name.split(".")[0]
    canvas_folder = get_canvas_folder(course, name_of_file)

    if css_path:
        global_css = css_path.read_text()
    else:
        global_css = ''

    def markdown_processor(text):
        return process_markdown(text, course, canvas_folder, file_path.parent, global_css)

    if "yaml" in file_path.name:
        walker = DocumentWalker(
            path_to_resources=file_path.parent,
            path_to_canvas_files=file_path.parent,
            markdown_processor=markdown_processor,
            time_zone=time_zone,
            group_identifier=lambda group_name: get_group_id(course, group_name, names_to_ids)
        )
        document = parse_yaml(content)
        document_object = walker.walk(document)
    else:
        # Provide processing functions, so that the parser needs no access to a canvas course
        parser = DocumentParser(
            path_to_resources=file_path.parent,
            path_to_canvas_files=file_path.parent,
            markdown_processor=markdown_processor,
            time_zone=time_zone,
            group_identifier=lambda group_name: get_group_id(course, group_name, names_to_ids),
        )
        document_object = parser.parse(content)

    # Create multiple quizzes or assignments from the document object
    for element in document_object:
        if "resources" in element:
            element = upload_and_link_files(element, course, element["resources"], course_folders)
        if "settings" in element:
            fix_dates(element["settings"], time_zone)
        if element["type"] == "quiz":
            modify_quiz(course, element, delete)
        elif element["type"] == "assignment":
            modify_assignment(course, element, delete)
        elif element["type"] == "page":
            modify_page(course, element, delete)
        elif element["type"] == "module":
            modify_module(course, element)
        elif element["type"] == "override":
            modify_override(course, element, time_zone)
        else:
            raise ValueError(f"Unknown type {element['type']}")


def get_course(api_url: str, api_token: str, canvas_course_id: int) -> Course:
    """
    Returns a Canvas Course object for the given API URL, API token, and course ID.

    :param api_url: str: The URL for the Canvas API.
    :param api_token: str: The authentication token for the Canvas API.
    :param canvas_course_id: int: The ID of the Canvas course.
    :return: Course: A Canvas Course object.
    """
    canvas = Canvas(api_url, api_token)
    course: Course = canvas.get_course(canvas_course_id)
    return course
