import requests
from klazor_client import settings
from klazor_client import utils


def config(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.items():
            if key == 'API_URL':
                settings.API_URL = value
            elif key == 'LOGIN':
                settings.LOGIN = value
            elif key == 'PASSWORD':
                settings.PASSWORD = value


def fetch_courses():
    courses_url = settings.API_URL + '/course/'
    auth_values = (settings.LOGIN, settings.PASSWORD)
    response = requests.get(courses_url, auth=auth_values)
    return utils.courses_from_dict(response.json())


def fetch_sheets():
    sheets_url = settings.API_URL + '/sheet/'
    auth_values = (settings.LOGIN, settings.PASSWORD)
    response = requests.get(sheets_url, auth=auth_values)
    return utils.sheets_from_dict(response.json())


def fetch_course(id):
    course_url = settings.API_URL + '/course/' + str(id)
    auth_values = (settings.LOGIN, settings.PASSWORD)
    response = requests.get(course_url, auth=auth_values)
    return utils.course_from_dict(response.json())


def fetch_sheet(id):
    sheet_url = settings.API_URL + '/sheet/' + str(id)
    auth_values = (settings.LOGIN, settings.PASSWORD)
    response = requests.get(sheet_url, auth=auth_values)
    return utils.sheet_from_dict(response.json())


def fetch_instructor(id):
    instructor_url = settings.API_URL + '/instructor/' + str(id)
    auth_values = (settings.LOGIN, settings.PASSWORD)
    response = requests.get(instructor_url, auth=auth_values)
    return utils.instructor_from_dict(response.json())


def fetch_instructors():
    instructor_url = settings.API_URL + '/instructor/'
    auth_values = (settings.LOGIN, settings.PASSWORD)
    response = requests.get(instructor_url, auth=auth_values)
    return utils.instructors_from_dict(response.json())
