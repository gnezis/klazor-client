from klazor_client import models



def sheets_from_dict(data):
    sheets = []
    for sheet_data in data:
        sheets.append(sheet_from_dict(sheet_data))
    return sheets

def sheet_from_dict(data):
    id = data['id']
    title = data['name']
    updated_at = data['updated_at']
    cells = []

    cells_data = data['cell_set']
    for cell_dict in cells_data:
        cells.append(cell_from_dict(cell_dict))
    return models.Sheet(id, title, cells, updated_at)


def cell_from_dict(data):
    if 'text' in data:
        return markdowncell_from_dict(data)
    elif 'Image' in data['type']:
        return imagecell_from_dict(data)
    elif 'video' in data:
        return videocell_from_dict(data)
    elif 'youtube' in data:
        return youtubecell_from_dict(data)
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
    url = data['url']
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


def youtubecell_from_dict(data):
    id = data['id']
    sequence = data['sequence']
    title = data['title']
    url = data['youtube']
    scale = data['scale']
    return models.YoutubeCell(id, sequence, title, url, scale)
