from categories.models import Category
from discounts.models import Discount
from django.test import TestCase
from faker import Faker
from products.models import Product
from users.models import User
from wishlists.models import Wishlist

fake = Faker()


class WishlistTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user_test = {
            "first_name": fake.name(),
            "last_name": fake.name(),
            "username": "kenzinho",
            "email": "kenzinho@gmail.com",
            "birthdate": "1999-09-09",
        }
        cls.product_test = {
            "name": fake.name(),
            "description": "lore ipsum est",
            "quantity": 20,
            "price": 14.20,
        }
        cls.category_test = {"name": fake.name()}
        cls.discount_test = {"description": "lore ipsum est", "discount_percent": 0.5}
        cls.user = User.objects.create(**cls.user_test)
        cls.discount = Discount.objects.create(**cls.discount_test)
        cls.category = Category.objects.create(**cls.category_test)
        cls.product = Product.objects.create(
            **cls.product_test, discount_id=1, category_id=1
        )
        cls.wishlist = Wishlist.objects.create(user=cls.user, product=cls.product)

    def test_relation_with_user(self):

        self.assertIs(
            self.wishlist.user, self.user, "testando relação de wishlist com user"
        )

    def test_relation_with_product(self):

        self.assertIs(
            self.wishlist.product,
            self.product,
            "testando relação de wishlist com product",
        )
