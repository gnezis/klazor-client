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


def fetch_folders():
    folders_url = settings.API_URL + '/folder/'
    auth_values = (settings.LOGIN, settings.PASSWORD)
    response = requests.get(folders_url, auth=auth_values)
    return utils.folders_from_dict(response.json())


def fetch_sheets():
    sheets_url = settings.API_URL + '/sheet/'
    auth_values = (settings.LOGIN, settings.PASSWORD)
    response = requests.get(sheets_url, auth=auth_values)
    return utils.sheets_from_dict(response.json())


def fetch_folder(id):
    folder_url = settings.API_URL + '/folder/' + str(id)
    auth_values = (settings.LOGIN, settings.PASSWORD)
    response = requests.get(folder_url, auth=auth_values)
    return utils.folder_from_dict(response.json())


def fetch_sheet(id):
    sheet_url = settings.API_URL + '/sheet/' + str(id)
    auth_values = (settings.LOGIN, settings.PASSWORD)
    response = requests.get(sheet_url, auth=auth_values)
    return utils.sheet_from_dict(response.json())
