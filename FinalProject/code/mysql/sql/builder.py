from mysql.sql.models import New_User


class MysqlBuilder:
    def __init__(self, client):
        self.client = client
        self.New_user = New_User.__table__

    def add_user(self, username, name, surname, password, email, access=1, active=0, middlename=None):
        new_user = New_User(
            username=username,
            name=name,
            surname=surname,
            password=password,
            email=email,
            access=access,
            active=active,
            middlename=middlename
        )
        self.client.session.add(new_user)
        self.client.session.commit()
        return new_user

