from categories.models import Category
from discounts.models import Discount
from django.test import TestCase
from faker import Faker
from products.models import Product

fake = Faker()


class ProductTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.product_test = {
            "name": fake.name(),
            "description": "lore ipsum est",
            "quantity": 20,
            "price": 14.20,
        }
        cls.category_test = {"name": fake.name()}
        cls.discount_test = {"description": "lore ipsum est", "discount_percent": 0.5}
        cls.discount = Discount.objects.create(**cls.discount_test)
        cls.category = Category.objects.create(**cls.category_test)
        cls.product = Product.objects.create(
            **cls.product_test, discount_id=cls.discount.id, category_id=cls.category.id
        )

    def test_product_fields(self):

        self.assertEqual(
            self.product.name, self.product_test["name"], "verificando name"
        )
        self.assertEqual(
            self.product.description,
            self.product_test["description"],
            "verificando description",
        )
        self.assertEqual(
            self.product.quantity, self.product_test["quantity"], "verificando quantity"
        )
        self.assertEqual(
            self.product.price, self.product_test["price"], "verificando price"
        )

    def test_relation_with_discount(self):

        self.assertIs(
            self.product.discount, self.discount, "verificando relação product/discount"
        )

    def test_relation_with_category(self):

        self.assertIs(
            self.product.category, self.category, "verificando relação product/category"
        )
