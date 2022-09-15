from django.test import TestCase
from users.models import User
from orders.models import Order
from faker import Faker

fake = Faker()

class OrderTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.order_test = {        
            "order_total": 0,
            "created_at": 2022-3-10,
        }
        cls.user_test = {
            "first_name": fake.name(),
            "last_name": fake.name(),
            "username": "kenzinho",
            "email": "kenzinho@gmail.com",
            "birthdate": "1999-09-09",
        }

        cls.user = User.objects.create(**cls.user_test)
        cls.order = Order.objects.create(**cls.order_test, user=cls.user)

    def test_relation_with_user(self):

        self.assertIs(self.order.user, self.user, 'testando relação de order com user')

    def test_order_fields(self):

        self.assertEqual(self.order.order_total, self.order_test["order_total"], 'verificando order_total')
        self.assertEqual(self.order.created_at, self.order_test["created_at"], 'verificando created_at')