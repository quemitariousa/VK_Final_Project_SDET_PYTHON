import faker

fake = faker.Faker()


class Builder:

    @staticmethod
    def fake_name() -> str:
        return fake.name()

    @staticmethod
    def fake_password() -> str:
        return fake.password()

    @staticmethod
    def fake_email() -> str:
        return fake.email()
