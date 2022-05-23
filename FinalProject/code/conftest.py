from mysql.sql.builder import MysqlBuilder
from mysql.sql.client import MysqlClient
from ui.fixtures import *


class MySql:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_client):
        self.client: MysqlClient = mysql_client
        self.builder: MysqlBuilder = MysqlBuilder(self.client)


@pytest.fixture(scope='session')
def mysql_client() -> MysqlClient:
    client = MysqlClient(db_name='basefinalproject')
    client.connect()
    yield client
    client.connection.close()


@pytest.fixture(scope='session')
def mysql_builder() -> MysqlBuilder:
    return MysqlBuilder(mysql_client)


def pytest_configure(config):
    if not hasattr(config, 'workerinput'):
        mysql_client = MysqlClient(db_name='basefinalproject')
        mysql_client.create_db()
        mysql_client.connect(db_created=True)
        mysql_client.create_table("test_users")
        mysql_client.connection.close()
