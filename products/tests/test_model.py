from django.test import TestCase
from products.models import Product
from faker import Faker

fake = Faker()

class ProductTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.product_test = {
            "name": fake.name(),
            "description": "lore ipsum est",
            "quantity": 20,
            "price": 14.20,
            "discount_id": 1,
            "category_id": 1
        }

        cls.product = Product.objects.create(**cls.product_test)

    def test_product_fields(self):

        self.assertEqual(self.product.name, self.product_test["name"], 'verificando name')
        self.assertEqual(self.product.description, self.product_test["description"], 'verificando description')
        self.assertEqual(self.product.quantity, self.product_test["quantity"], 'verificando quantity')
        self.assertEqual(self.product.price, self.product_test["price"], 'verificando price')
        self.assertEqual(self.product.discount_id, self.product_test["discount_id"], 'verificando discount_id')
        self.assertEqual(self.product.category_id, self.product_test["category_id"], 'verificando category_id')
