class Model:
    def __init__(self, id):
        self.id = id

class Item(Model):
    def __init__(self, id, name):
        super().__init__(id)
        self.name = name


class File(Item):
    def __init__(self, id, url, name):
        super().__init__(id, name)
        self.url = url

class Sheet(Item):
    def __init__(self, id, name, cells, updated_at):
        super().__init__(id, name)
        self.cells = cells
        self.updated_at = updated_at



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
        elif isinstance(self, YoutubeCell):
            return 'youtube'
        elif isinstance(self, ImageCell):
            return 'image'
        elif isinstance(self, AudioCell):
            return 'audio'
        elif isinstance(self, MultipleChoiceInputCell):
            return 'mcq'


class MarkdownCell(Cell):
    def __init__(self, id, sequence, text):
        super().__init__(id, sequence)
        self.text = text


class Proposition():
    def __init__(self, id, statement, is_true):
        self.id = id
        self.statement = statement
        self.is_true = is_true


class MultipleChoiceInputCell(Cell):
    def __init__(self, id, sequence, propositions):
        super().__init__(id, sequence)
        self.propositions = propositions

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


class YoutubeCell(GraphicMediaCell):
    pass
