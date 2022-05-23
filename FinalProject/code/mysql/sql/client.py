import os

import sqlalchemy
from sqlalchemy import inspect
from sqlalchemy.orm import sessionmaker

from mysql.sql.models import Base, New_User


class MysqlClient:

    def __init__(self, db_name):
        # self.user = os.environ['USER']
        # self.port = os.environ['PORT']
        #
        # self.password = os.environ['PASSWORD']
        # self.host = os.environ['HOST']

        self.user = 'test_qa'
        self.port = 3306
        self.password = 'qa_test'
        self.host = 'mysql'

        self.db_name = db_name

        self.connection = None
        self.engine = None
        self.session = None

    def connect(self, db_created=True):
        db = self.db_name if db_created else ''
        url = f'mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{db}'
        self.engine = sqlalchemy.create_engine(url, max_overflow=5)
        self.connection = self.engine.connect()

        session = sessionmaker(bind=self.connection.engine)
        self.session = session()

    def create_db(self):
        self.connect(db_created=False)
        self.execute_query(f'DROP database IF EXISTS {self.db_name}')
        self.execute_query(f'CREATE database {self.db_name}')

    def execute_query(self, query, fetch=False):
        res = self.connection.execute(query)
        if fetch:
            return res.fetchall()

    def create_table(self, table_name):
        if not inspect(self.engine).has_table(table_name):
            Base.metadata.tables[table_name].create(self.engine)
            self.execute_query(
                f"INSERT INTO {table_name}(name, surname, middle_name, username, password, email, access, active, start_active_time)"
                f"VALUES ('Lera', 'Lerusha', 'Lerchanskia', 'quemitariousa6', 'ilovebordercollie', 'quemitariousa6@gmail.com', NULL ,NULL, NULL)")

    def get_users(self, **filters):
        self.session.commit()
        res = self.session.query(New_User).filter_by(**filters)
        return res.all()

    def get_users_by_username(self, username):
        return self.get_users(**{"username": username})

    def get_current_user(self):
        return self.get_users(**{"active": 1})

    def delete_user_by_username(self, username):
        self.get_users(**{"username": username}).delete()