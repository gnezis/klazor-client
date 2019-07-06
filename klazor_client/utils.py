from klazor_client import models


def course_from_dict(data):
    id = data['id']
    title = data['title']
    topics = []
    instructors = []
    resources = []
    parts = []

    topics_data = data['topic_set']
    for topic_dict in topics_data:
        topics.append(topic_from_dict(topic_dict))

    parts_data = data['coursepart_set']
    for part_dict in parts_data:
        parts.append(course_part_from_dict(part_dict))

    resources_data = data['resource_set']
    for resource_dict in resources_data:
        resources.append(resource_from_dict(resource_dict))

    instructors_data = data['instructor_set']
    for instructor_dict in instructors_data:
        instructors.append(instructor_from_dict(instructor_dict))

    return models.Course(id, title, topics, instructors, resources, parts)


def courses_from_dict(data):
    courses = []
    for course_data in data:
        courses.append(course_from_dict(course_data))
    return courses


def sheets_from_dict(data):
    sheets = []
    for sheet_data in data:
        sheets.append(sheet_from_dict(sheet_data))
    return sheets


def resource_from_dict(data):
    id = data['id']
    url = data['file']
    title = data['title']
    return models.File(id, url, title)


def instructor_from_dict(data):
    id = data['id']
    name = data['name']
    link = data['link']
    if 'colloquial_name' in data:
        colloquial_name = data['colloquial_name']
        return models.School(id, name, link, colloquial_name)
    return models.NotSchool(id, name, link)


def instructors_from_dict(data):
    instructors = []
    for instructor_data in data:
        instructors.append(instructor_from_dict(instructor_data))
    return instructors


def topic_from_dict(data):
    id = data['id']
    title = data['title']
    return models.Topic(id, title)


def course_part_from_dict(data):
    id = data['id']
    label = data['label']
    title = data['title']
    level = data['level']
    sequence = data['sequence']
    elements = []

    elements_data = data['courseelement_set']
    for element_dict in elements_data:
        elements.append(course_element_from_dict(element_dict))
    return models.CoursePart(id, label, title, level, sequence, elements)


def course_element_from_dict(data):
    id = data['id']
    title = data['title']
    sequence = data['sequence']
    cells = []

    cells_data = data['cell_set']
    for cell_dict in cells_data:
        cells.append(cell_from_dict(cell_dict))
    return models.CourseElement(id, title, cells, sequence)


def sheet_from_dict(data):
    id = data['id']
    title = data['title']
    cells = []

    cells_data = data['cell_set']
    for cell_dict in cells_data:
        cells.append(cell_from_dict(cell_dict))
    return models.Sheet(id, title, cells)


def cell_from_dict(data):
    if 'text' in data:
        return markdowncell_from_dict(data)
    elif 'image' in data:
        return imagecell_from_dict(data)
    elif 'video' in data:
        return videocell_from_dict(data)
    elif 'audio' in data:
        return audiocell_from_dict(data)


def markdowncell_from_dict(data):
    id = data['id']
    sequence = data['sequence']
    text = data['text']
    return models.MarkdownCell(id, sequence, text)


def imagecell_from_dict(data):
    id = data['id']
    sequence = data['sequence']
    title = data['title']
    url = data['image']
    scale = data['scale']

    return models.ImageCell(id, sequence, title, url, scale)


def audiocell_from_dict(data):
    id = data['id']
    sequence = data['sequence']
    title = data['title']
    url = data['audio']

    return models.AudioCell(id, sequence, title, url)


def videocell_from_dict(data):
    id = data['id']
    sequence = data['sequence']
    title = data['title']
    url = data['video']
    scale = data['scale']

    return models.VideoCell(id, sequence, title, url, scale)
