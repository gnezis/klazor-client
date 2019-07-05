class Topic:
    def __init__(self, title):
        self.title = title


class Instructor:
    def __init__(self, title, link):
        self.title = title
        self.link = link


class Item:
    def __init__(self, title):
        self.title = title


class File(Item):
    def __init__(self, url, title):
        super().__init__(title)
        self.url = url


class Course(Item):
    def __init__(self, title, topics, instructors, resources, parts):
        super().__init__(title)
        self.topics = topics
        self.instructors = instructors
        self.resources = resources
        self.parts = parts


class Sheet(Item):
    def __init__(self, title, cells):
        super().__init__(title)
        self.cells = cells


class CourseElement(Sheet):
    def __init__(self, title, cells, sequence):
        super().__init__(title, cells)
        self.sequence = sequence


class MoocCourse(Course):
    pass


class SchoolCourse(Course):
    def __init__(self, title, topics, instructors, resources, year, semester):
        super().__init__(title, topics, instructors, resources)
        self.year = year
        self.semester = semester


class CoursePart:
    def __init__(self, label, title, level, sequence, elements):
        self.label = label
        self.title = title
        self.level = level
        self.sequence = sequence
        self.elements = elements


class Cell:
    def __init__(self, sequence):
        self.sequence = sequence


class MarkdownCell(Cell):
    def __init__(self, sequence, text):
        super().__init__(sequence)
        self.text = text


class MediaCell(Cell):
    def __init__(self, sequence, title, url):
        super().__init__(sequence)
        self.title = title
        self.url = url


class GraphicMediaCell(MediaCell):
    def __init__(self, sequence, title, url, scale):
        super().__init__(sequence, title, url)
        self.scale = scale


class VideoCell(GraphicMediaCell):
    pass


class AudioCell(MediaCell):
    pass


class ImageCell(GraphicMediaCell):
    pass
