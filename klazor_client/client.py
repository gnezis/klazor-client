import requests
from klazor_client import settings
from klazor_client import utils


def config(*args, **kwargs):
    if kwargs is not None:
        for key, value in kwargs.items():
            if key == 'API_URL':
                settings.API_URL = value


def connect(login, password):
    """ To implement
    :param login:
    :param password:
    """
    pass


def fetch_courses():
    courses_url = settings.API_URL + '/course/'
    response = requests.get(courses_url)
    return utils.courses_from_dict(response.json())


def fetch_sheets():
    sheets_url = settings.API_URL + '/sheet/'
    response = requests.get(sheets_url)
    return utils.sheets_from_dict(response.json())


def fetch_course(id):
    course_url = settings.API_URL + '/course/' + str(id)
    response = requests.get(course_url)
    return utils.course_from_dict(response.json())


def fetch_sheet(id):
    sheet_url = settings.API_URL + '/sheet/' + str(id)
    response = requests.get(sheet_url)
    return utils.sheet_from_dict(response.json())


def fetch_instructor(id):
    instructor_url = settings.API_URL + '/instructor/' + str(id)
    response = requests.get(instructor_url)
    return utils.instructor_from_dict(response.json())


def fetch_instructors():
    instructor_url = settings.API_URL + '/instructor/'
    response = requests.get(instructor_url)
    return utils.instructors_from_dict(response.json())
