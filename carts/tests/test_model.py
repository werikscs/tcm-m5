from django.test import TestCase
from carts.models import Cart


class CartTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.cart_test = {
            "subtotal": 30
        }
        cls.cart = Cart.objects.create(**cls.cart_test)

    def test_cart_fields(self):

        self.assertEqual(self.cart.subtotal, self.cart_test["subtotal"], 'verificando subtotal')
        
