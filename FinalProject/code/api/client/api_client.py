import logging
import pdb

import faker
import requests

from utils.builder import Builder

logger = logging.getLogger('test')

MAX_RESPONSE_LENGTH = 300


class InvalidLoginException(Exception):
    pass


class RespondErrorException(Exception):
    pass


class ResponseStatusCodeException(Exception):
    pass


fake = faker.Faker()


class ApiClient:

    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.session = requests.Session()


    #  общий метод для осуществления get и post запросов
    def _request(self, method, location, headers=None, data=None, params=None, json=None):
        url = location
        response = self.session.request(method=method, url=url, headers=headers, data=data, params=params, json=json)
        return response

    def post_login(self, login, password):
        url = 'http://test_app:8086/login'

        headers = {"Referer": url}

        data = {
            'username': login,
            'password': password
        }

        result = self._request('POST', location=url, headers=headers, data=data)

        return result

    def logout(self):
        url = 'http://test_app:8086/logout'
        result = self._request('GET', url)
        return result

    #TODO: как-то бля сделать кастомный юзер рандом
    def user_random(self, name, surname, username, email, password, middlename):
        print(name, surname, username, email, password, middlename)

        return {
            'name': name,
            'surname': surname,
            'username': username,
            'email': email,
            'password': password,
            'pass_repeat': password,
            'middlename': middlename,
        }

    def post_user(self, name=Builder.fake_name(), surname=Builder.fake_name(), middlename=Builder.fake_name(),
                    username=Builder.fake_name(), email=Builder.fake_email(), password=Builder.fake_password()):
        url = 'http://test_app:8086/api/user'
        headers = {"Content-Type": "application/json"}
        aboba = self.user_random(name, surname, username, email, password, middlename)
        data = {
            "name": aboba['name'],
            "surname": aboba['surname'],
            "middle_name": aboba['middlename'],
            "username": aboba['username'],
            "password": aboba['password'],
            "email": aboba['email']
        }

        result = self._request('POST', url, headers=headers, json=data)
        return result, data

    def delete_user(self, username):
        url = f"http://test_app:8086/api/user/{username}"
        result = self._request('DELETE', url)
        return result, username

    def block_user(self, username):
        url = f"http://test_app:8086/api/user/{username}/block"
        result = self._request('POST', url)
        return result, username

    def change_pw(self, username, pw):
        url = f'http://test_app:8086/api/user/{username}/change-password'
        data = {
            "password": pw
        }
        result = self._request("PUT", location=url, json=data)
        return result, pw

    def accept_user(self, username):
        url = f'http://test_app:8086/api/user/{username}/accept'
        result = self._request("POST", location=url)
        return result, username

    def check_status(self):
        url = "http://test_app:8086/status"
        result = self._request("GET", location=url)
        return result