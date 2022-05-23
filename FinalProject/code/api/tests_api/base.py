import pytest

from mysql.sql.builder import MysqlBuilder


class BaseApi:
    BLOG_ID = 403

    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, api_client, mysql_client):
        self.api_client = api_client

        self.mysql_client = mysql_client
        self.builder = MysqlBuilder(self.mysql_client)
