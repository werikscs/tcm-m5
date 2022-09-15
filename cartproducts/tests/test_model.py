from cartproducts.models import Cartproducts
from carts.models import Cart
from categories.models import Category
from discounts.models import Discount
from django.test import TestCase
from faker import Faker
from products.models import Product

fake = Faker()

class CartProductTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.cartprod_test = {
            "quantity_in_cart": 1,
        }
        cls.cart_test = {
            "name": fake.name()
        }
        cls.product_test = {
            "name": fake.name(),
            "description": "lore ipsum est",
            "quantity": 20,
            "price": 14.20,
        }
        cls.category_test = {
            "name": fake.name()
        }
        cls.discount_test = {
            "description": "lore ipsum est",
            "discount_percent": 0.5
        }

        cls.discount = Discount.objects.create(**cls.discount_test)
        cls.category = Category.objects.create(**cls.category_test)
        cls.product = Product.objects.create(**cls.product_test, discount_id=cls.discount_test.id, category_id=cls.category_test.id)
        cls.cart = Cart.objects.create(**cls.cart_test)
        cls.cartprod = Cartproducts.objects.create(**cls.cartprod_test, cart=cls.cart, product=cls.product)
    
    
    def test_relation_with_cart(self):

        self.assertIs(self.cartprod.cart, self.cart, 'verificando relação cartprod/cart')

    def test_relation_with_product(self):

        self.assertIs(self.cartprod.product, self.product, 'verificando relação cartprod/product')
