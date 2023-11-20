import configuration
import requests
import data

def create_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH, json=body)

def get_token():
    return create_token().json()["authToken"]


def create_token():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH, json=data.user_body)

def post_new_client_kit(kit_body):
    return requests.post(configuration.URL_SERVICE + configuration.KIT_PATH,
                         json=kit_body,
                         headers={"Authorization": "Bearer " + get_token()})
