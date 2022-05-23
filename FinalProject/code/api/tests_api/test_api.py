import allure

from api.tests_api.base import BaseApi
import pytest

from userdata import creds


class TestsStatus(BaseApi):
    @allure.epic('API tests')
    @allure.feature('Status')
    @allure.description('Проверка статуса приложения')
    def test_check_status(self):
        self.api_client.post_login(creds.login, creds.password)
        answer = self.api_client.check_status()
        assert answer.status_code == 200


@pytest.mark.nobrowser
class TestsAuth(BaseApi):

    @allure.epic('API tests')
    @allure.feature('Login')
    @allure.description('Проверка логина несуществующего пользователя ')
    @pytest.mark.xfail
    def test_auth_non_exist_user(self):
        answer = self.api_client.post_login("quemitariousa7@gmail.com", "heyheylalaley")
        assert answer.status_code == 404

    @allure.epic('API tests')
    @allure.feature('Login')
    @allure.description('Проверка логина c невалидным паролем')
    def test_auth_invalid_pw(self):
        answer = self.api_client.post_login(creds.login, "heyheylalaley")
        assert answer.status_code == 401

    # !!!! БАГ
    @allure.epic('API tests')
    @allure.feature('Login')
    @allure.description('Проверка логина c невалидным логином')
    @pytest.mark.xfail
    def test_auth_invalid_login(self):
        answer = self.api_client.post_login("123231231223", creds.password)
        assert answer.status_code == 404

    @allure.epic('API tests')
    @allure.feature('Login')
    @allure.description('Валидный пароль')
    def test_auth(self):
        answer = self.api_client.post_login(creds.login, creds.password)
        assert answer.status_code == 200


# !!!!!!!!!
# TODO: Поправить тесты, потому что чето дохуя багов))
class TestsCreateUser(BaseApi):
    # баг сущность создана 201, ТУТ 210 - баг
    @allure.epic('API tests')
    @allure.feature('Create user')
    @pytest.mark.xfail
    @allure.description('Проверка создания пользователя с валидным юзернеймом c middlename - БАГ')
    def test_correct_new_user_with_mn(self):
        self.api_client.post_login(creds.login, creds.password)
        answer = self.api_client.post_user()
        assert answer[0].status_code == 201
        assert answer[1]['username'] in self.mysql_client.get_users_by_username(answer[1]['username'])[0].username

    # баг сущность без middlename не создана (401)
    @allure.epic('API tests')
    @allure.feature('Create user')
    @allure.description('Проверка создания пользователя с валидным юзернеймом без middlename - БАГ')
    @pytest.mark.xfail
    def test_correct_username_new_user_without_mn(self):
        self.api_client.post_login(creds.login, creds.password)
        answer = self.api_client.post_user(middlename=None)
        assert answer[0].status_code == 201
        assert answer[1]['username'] in self.mysql_client.get_users_by_username(answer[1]['username'])[0].username

    # баг, получается 500, должна 400
    @allure.epic('API tests')
    @allure.feature('Create user')
    @allure.description('Проверка создания пользователя с невалидным юзернеймом - БАГ')
    @pytest.mark.parametrize("username", ["0", "TOOOLOOONGUSERNAAAMEE", " ", None],
                             ids=['short_username', "long_username", "none_username", "empty_username"])
    @pytest.mark.xfail
    def test_incorrect_username_new_user(self, username):
        self.api_client.post_login(creds.login, creds.password)
        answer = self.api_client.post_user(username=username)
        assert answer[0].status_code == 400
        assert answer[1]['username'] not in self.mysql_client.get_users_by_username(answer[1]['username'])[0].username

    # баг с none, должен быть 400, а идет 210
    @allure.epic('API tests')
    @allure.feature('Create user')
    @allure.description('Проверка создания пользователя с невалидным паролем - БАГ')
    @pytest.mark.parametrize("pw", [None, " ", ("NADO256SMV" * 100)],
                             ids=["none_pw", "empty_pw", "long_pw"])
    @pytest.mark.xfail
    def test_incorrect_pw_new_user(self, pw):
        self.api_client.post_login(creds.login, creds.password)
        answer = self.api_client.post_user(password=pw)
        assert answer[0].status_code == 400
        assert answer[1]['username'] not in self.mysql_client.get_users_by_username(answer[1]['username'])[0].username

    # баг на слишком мелкий емейл, создается 210, но должен 400 из-за отсутствия как минимум собаки
    @allure.epic('API tests')
    @allure.feature('Create user')
    @allure.description('Проверка создания пользователя с невалидным email - БАГ')
    @pytest.mark.parametrize("email",
                             ["0", "NADO256SIMVOLOVSORRYBRATISHKANADO256SIMVOLOVSORRYBRATISHKANADO256S@yopta.com",
                              " ", None],
                             ids=['short_email', "long_email", "none_email", "empty_email"])
    @pytest.mark.xfail
    def test_incorrect_email_new_user(self, email):
        self.api_client.post_login(creds.login, creds.password)
        answer = self.api_client.post_user(email=email)
        assert answer[0].status_code == 400
        assert answer[1]['username'] not in self.mysql_client.get_users_by_username(answer[1]['username'])[0].username

    # баг на пустоту и короткий
    @allure.epic('API tests')
    @allure.feature('Create user')
    @allure.description('Проверка создания пользователя с невалидным именем  - БАГ')
    @pytest.mark.parametrize("name", [None, " ", (
            "NADO256SIMVOLOVSORRY" * 100)],
                             ids=["none_name", "empty_name", "long_name"])
    @pytest.mark.xfail
    def test_incorrect_name_new_user(self, name):
        self.api_client.post_login(creds.login, creds.password)
        answer = self.api_client.post_user(name=name)
        assert answer[0].status_code == 400
        assert answer[1]['username'] not in self.mysql_client.get_users_by_username(answer[1]['username'])[0].username

    # баг на пустоту и короткий
    @allure.epic('API tests')
    @allure.feature('Create user')
    @allure.description('Проверка создания пользователя с невалидным surname  - БАГ')
    @pytest.mark.parametrize("surname", [None, "1", (
            "NADO256SIMVOLOVSORRY" * 100)],
                             ids=["none_surname", "empty_surname", "long_surname"])
    @pytest.mark.xfail
    def test_incorrect_surname(self, surname):
        self.api_client.post_login(creds.login, creds.password)
        answer = self.api_client.post_user(surname=surname)
        assert answer[0].status_code == 400
        assert answer[1]['username'] not in self.mysql_client.get_users_by_username(answer[1]['username'])[0].username

    # баг на пустоту и короткий
    @allure.epic('API tests')
    @allure.feature('Create user')
    @allure.description('Проверка создания пользователя с невалидным middlename  - БАГ')
    @pytest.mark.parametrize("middlename", ["1", (
            "NADO256SIMVOLOVSORRY" * 100)],
                             ids=["empty_middlename", "long_middlename"])
    @pytest.mark.xfail
    def test_incorrect_middlename(self, middlename):
        self.api_client.post_login(creds.login, creds.password)
        answer = self.api_client.post_user(middlename=middlename)
        assert answer[0].status_code == 400
        assert answer[1]['username'] not in self.mysql_client.get_users_by_username(answer[1]['username'])[0].username


class TestsDeleteUser(BaseApi):
    @allure.epic('API tests')
    @allure.feature('Delete')
    @allure.description('Проверка корректного удаления юзера')
    def test_correct_delete_user(self):
        self.api_client.post_login(creds.login, creds.password)
        user = self.api_client.post_user()
        username = user[1].get('username')
        answer = self.api_client.delete_user(username)
        assert answer[0].status_code == 204
        assert answer[1] not in self.mysql_client.get_users_by_username(answer[1])

    @allure.epic('API tests')
    @allure.feature('Delete')
    @allure.description('Проверка удаления несуществующего юзера')
    def test_not_exist_user(self):
        self.api_client.post_login(creds.login, creds.password)
        user = self.api_client.post_user()
        username = user[1].get('username')
        self.api_client.delete_user(username)
        answer = self.api_client.delete_user(username)
        assert answer[0].status_code == 404
        assert answer[1] not in self.mysql_client.get_users_by_username(answer[1])


class TestsChangePw(BaseApi):

    # !!! 204 получается - баг
    @allure.epic('API tests')
    @allure.feature('Change pw')
    @allure.description('Проверка корректной смены пароля - БАГ')
    @pytest.mark.xfail
    def test_correct_change_pw_user(self):
        self.api_client.post_login(creds.login, creds.password)
        user = self.api_client.post_user()
        username = user[1].get('username')
        answer = self.api_client.change_pw(username, 'new_pw')
        assert answer[0].status_code == 200
        assert 'new_pw' in self.mysql_client.get_users_by_username(username)[0].password

    @allure.epic('API tests')
    @allure.feature('Change pw')
    @allure.description('Проверка смены пароля у несуществующего пользователя')
    def test_correct_change_pw_user_not_exist(self):
        self.api_client.post_login(creds.login, creds.password)
        user = self.api_client.post_user()
        username = user[1].get('username')
        self.api_client.delete_user(username)
        answer = self.api_client.change_pw(username, 'new_pw')
        assert answer[0].status_code == 404
        assert username not in self.mysql_client.get_users_by_username(username)


class TestsBlockUser(BaseApi):
    @allure.epic('API tests')
    @allure.feature('Block')
    @allure.description('Проверка корректной блокировки')
    def test_correct_block_user(self):
        self.api_client.post_login(creds.login, creds.password)
        user = self.api_client.post_user()
        username = user[1].get('username')
        answer = self.api_client.block_user(username)
        assert answer[0].status_code == 200
        assert 0 == self.mysql_client.get_users_by_username(username)[0].access

    @allure.epic('API tests')
    @allure.feature('Block')
    @allure.description('Проверка блокировки несуществующего пользователя')
    def test_correct_block_not_exist_user(self):
        self.api_client.post_login(creds.login, creds.password)
        user = self.api_client.post_user()
        username = user[1].get('username')
        self.api_client.delete_user(username)
        answer = self.api_client.block_user(username)
        assert answer[0].status_code == 404
        assert username not in self.mysql_client.get_users_by_username(username)

    @allure.epic('API tests')
    @allure.feature('Block')
    @allure.description('Проверка блокировки пользователя, который уже в блоке')
    def test_block_blocked_user(self):
        self.api_client.post_login(creds.login, creds.password)
        user = self.api_client.post_user()
        username = user[1].get('username')
        self.api_client.block_user(username)
        answer = self.api_client.block_user(username)
        assert answer[0].status_code == 400
        assert 0 == self.mysql_client.get_users_by_username(username)[0].access


class TestsUnblockUser(BaseApi):
    @allure.epic('API tests')
    @allure.feature('Unblock')
    @allure.description('Проверка корректной разблокировки')
    def test_correct_unblock_user(self):
        self.api_client.post_login(creds.login, creds.password)
        user = self.api_client.post_user()
        username = user[1].get('username')
        self.api_client.block_user(username)
        answer = self.api_client.accept_user(username)
        assert answer[0].status_code == 200
        assert 1 == self.mysql_client.get_users_by_username(username)[0].access

    @allure.epic('API tests')
    @allure.feature('Unblock')
    @allure.description('Проверка разблокировки несуществующего пользователя')
    def test_incorrect_unblock_not_exist_user(self):
        self.api_client.post_login(creds.login, creds.password)
        user = self.api_client.post_user()
        username = user[1].get('username')
        self.api_client.delete_user(username)
        self.api_client.block_user(username)
        answer = self.api_client.accept_user(username)
        assert answer[0].status_code == 404
        assert username not in self.mysql_client.get_users_by_username(username)

    # ???
    @allure.epic('API tests')
    @allure.feature('Unblock')
    @allure.description('Проверка разблокировки пользователя, который не в блоке')
    def test_incorrect_unblock_not_blocked_user(self):
        self.api_client.post_login(creds.login, creds.password)
        user = self.api_client.post_user()
        username = user[1].get('username')
        answer = self.api_client.accept_user(username)
        assert answer[0].status_code == 400
        assert 1 == self.mysql_client.get_users_by_username(username)[0].access
