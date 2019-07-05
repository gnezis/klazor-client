from klazor_client import models


def course_from_dict(data):
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

    # resources_data = data['resources_set']
    # for resource_dict in resources_data:
    #     resources.append(resource_from_dict(resource_dict))
    #
    # instructors_data = data['instructors_set']
    # for instructor_dict in instructors_data:
    #     instructors.append(instructor_from_dict(instructor_dict))
    #
    return models.Course(title, topics, instructors, resources, parts)


def resource_from_dict(data):
    pass


def instructor_from_dict(data):
    pass


def topic_from_dict(data):
    title = data['title']
    return models.Topic(title)


def course_part_from_dict(data):
    label = data['label']
    title = data['title']
    level = data['level']
    sequence = data['sequence']
    elements = []

    elements_data = data['courseelement_set']
    for element_dict in elements_data:
        elements.append(course_element_from_dict(element_dict))
    return models.CoursePart(label, title, level, sequence, elements)


def course_element_from_dict(data):
    title = data['title']
    sequence = data['sequence']
    cells = []

    cells_data = data['cell_set']
    for cell_dict in cells_data:
        cells.append(cell_from_dict(cell_dict))
    return models.CourseElement(title, cells, sequence)


def sheet_from_dict(data):
    title = data['title']
    cells = []

    cells_data = data['cell_set']
    for cell_dict in cells_data:
        cells.append(cell_from_dict(cell_dict))
    return models.Sheet(title, cells)


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
    sequence = data['sequence']
    text = data['text']

    return models.MarkdownCell(sequence, text)


def imagecell_from_dict(data):
    sequence = data['sequence']
    title = data['title']
    url = data['image']
    scale = data['scale']

    return models.ImageCell(sequence, title, url, scale)


def audiocell_from_dict(data):
    sequence = data['sequence']
    title = data['title']
    url = data['audio']

    return models.AudioCell(sequence, title, url)


def videocell_from_dict(data):
    sequence = data['sequence']
    title = data['title']
    url = data['video']
    scale = data['scale']

    return models.VideoCell(sequence, title, url, scale)
