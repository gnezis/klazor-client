class Model:
    def __init__(self, id):
        self.id = id


class Topic(Model):
    def __init__(self, id, title):
        super().__init__(id)
        self.title = title


class Instructor(Model):
    def __init__(self, id, name, link):
        super().__init__(id)
        self.name = name
        self.link = link


class School(Instructor):
    def __init__(self, id, name, link, colloquial_name):
        super().__init__(id, name, link)
        self.colloquial_name = colloquial_name


class NotSchool(Instructor):
    pass


class Item(Model):
    def __init__(self, id, title):
        super().__init__(id)
        self.title = title


class File(Item):
    def __init__(self, id, url, title):
        super().__init__(id, title)
        self.url = url


class Course(Item):
    def __init__(self, id, title, topics, instructors, resources, parts):
        super().__init__(id, title)
        self.topics = topics
        self.instructors = instructors
        self.resources = resources
        self.parts = parts


class Sheet(Item):
    def __init__(self, id, title, cells):
        super().__init__(id, title)
        self.cells = cells


class CourseElement(Sheet):
    def __init__(self, id, title, cells, sequence):
        super().__init__(id, title, cells)
        self.sequence = sequence


class MoocCourse(Course):
    pass


class SchoolCourse(Course):
    def __init__(self, id, title, topics, instructors, resources, year, semester):
        super().__init__(id, title, topics, instructors, resources)
        self.year = year
        self.semester = semester


class CoursePart(Model):
    def __init__(self, id, label, title, level, sequence, elements):
        super().__init__(id)
        self.label = label
        self.title = title
        self.level = level
        self.sequence = sequence
        self.elements = elements


class Cell(Model):
    def __init__(self, id, sequence):
        super().__init__(id)
        self.sequence = sequence

    @property
    def type(self):
        if isinstance(self, MarkdownCell):
            return 'markdown'
        elif isinstance(self, VideoCell):
            return 'video'
        elif isinstance(self, ImageCell):
            return 'image'
        elif isinstance(self, AudioCell):
            return 'audio'


class MarkdownCell(Cell):
    def __init__(self, id, sequence, text):
        super().__init__(id, sequence)
        self.text = text


class MediaCell(Cell):
    def __init__(self, id, sequence, title, url):
        super().__init__(id, sequence)
        self.title = title
        self.url = url


class GraphicMediaCell(MediaCell):
    def __init__(self, id, sequence, title, url, scale):
        super().__init__(id, sequence, title, url)
        self.scale = scale


class VideoCell(GraphicMediaCell):
    pass


class AudioCell(MediaCell):
    pass


class ImageCell(GraphicMediaCell):
    pass
