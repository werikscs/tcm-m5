from django.test import TestCase
from categories.models import Category
from faker import Faker

fake = Faker()

class CategoryTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.category_test = {
            "name": fake.name()
        }
        cls.category = Category.objects.create(**cls.category_test)

    def test_category_fields(self):

        self.assertEqual(self.category.name, self.category_test["name"], 'verificando name')
        
