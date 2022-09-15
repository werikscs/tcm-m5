from django.test import TestCase
from users.models import User
from faker import Faker

fake = Faker()

class UserTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user_test = {
            "first_name": fake.name(),
            "last_name": fake.name(),
            "username": "kenzinho",
            "email": "kenzinho@gmail.com",
            "birthdate": "1999-09-09",
        }
        cls.user = User.objects.create(**cls.user_test)

    def test_user_fields(self):

        self.assertEqual(self.user.first_name, self.user_test["first_name"], 'verificando first name')
        self.assertEqual(self.user.last_name, self.user_test["last_name"], 'verificando last name')
        self.assertEqual(self.user.username, self.user_test["username"], 'verificando username')
        self.assertEqual(self.user.email, self.user_test["email"], 'verificando email')
        self.assertEqual(self.user.birthdate, self.user_test["birthdate"], 'verificando birthdate')