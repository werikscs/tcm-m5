from django.test import TestCase
from discounts.models import Discount
from faker import Faker

fake = Faker()

class DiscountTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.discount_test = {
            "description": "lore ipsum est",
            "discount_percent": fake.decimal()
        }
        cls.discount = Discount.objects.create(**cls.discount_test)

    def test_discount_fields(self):

        self.assertEqual(self.discount.description, self.discount_test["description"], 'verificando description')
        self.assertEqual(self.discount.discount_percent, self.discount_test["discount_percent"], 'verificando discount_percent')
        
