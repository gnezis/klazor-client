import requests
from klazor_client import settings


def config(*args, **kwargs):
    if kwargs is not None:
        for key, value in kwargs.items():
            if key == 'API_URL':
                settings.API_URL = value


def connect(login, password):
    pass


def fetch_course(course_id):
    course_url = settings.API_URL + '/course/' + str(course_id)
    response = requests.get(course_url)

    return response.json()
