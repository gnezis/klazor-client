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
    def __init__(self, title, topics, instructors, resources):
        super().__init__(title)
        self.topics = topics
        self.instructors = instructors
        self.resources = resources


class Sheet(Item):
    def __init___(self, title, cells):
        super().__init__(title)
        self.cells = cells


class CourseElement(Sheet):
    def __init___(self, title, cells, sequence, course_part):
        super().__init__(title, cells)
        self.sequence = sequence
        self.course_part = course_part


class MoocCourse(Course):
    pass


class SchoolCourse(Course):
    def __init__(self, title, topics, instructors, resources, year, semester):
        super().__init__(title, topics, instructors, resources)
        self.year = year
        self.semester = semester


class CoursePart:
    def __init__(self, label, title, course, level, sequence):
        self.label = label
        self.title = title
        self.course = course
        self.level = level
        self.sequence = sequence


class Cell:
    def __init__(self, sequence, sheet):
        self.sequence = sequence
        self.sheet = sheet


class MarkdownCell(Cell):
    def __init__(self, sequence, sheet, text):
        super().__init__(sequence, sheet)
        self.text = text


class MediaCell(Cell):
    def __init__(self, sequence, sheet, title, url):
        super().__init__(sequence, sheet)
        self.title = title
        self.url = url


class GraphicMediaCell(MediaCell):
    def __init__(self, sequence, sheet, title, url, scale):
        super().__init__(sequence, sheet, title, url)
        self.scale = scale


class VideoCell(GraphicMediaCell):
    pass


class AudioCell(MediaCell):
    pass


class ImageCell(GraphicMediaCell):
    pass
