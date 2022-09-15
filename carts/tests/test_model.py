from django.test import TestCase
from carts.models import Cart

from users.models import User
from faker import Faker
fake = Faker()

class CartTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.cart_test = {
            "subtotal": 30
        }

        cls.user_test = {
            "first_name": fake.name(),
            "last_name": fake.name(),
            "username": "kenzinho",
            "email": "kenzinho@gmail.com",
            "birthdate": "1999-09-09",
        }
        cls.user = User.objects.create(**cls.user_test)
        cls.cart = Cart.objects.create(**cls.cart_test, user = cls.user)


    def test_cart_fields(self):

        self.assertEqual(self.cart.subtotal, self.cart_test["subtotal"], 'verificando subtotal')



    def test_relation_with_user(self):

        self.assertIs(self.cart.user, self.user, 'verificando relação com user')
        


        
