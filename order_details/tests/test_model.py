from categories.models import Category
from discounts.models import Discount
from django.test import TestCase
from faker import Faker
from order_details.models import OrderDetails
from orders.models import Order
from products.models import Product
from users.models import User

fake = Faker()


class OrderDetailTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.orderdetail_test = {
            "final_price": 10,
            "quantity_in_order": 0,
        }
        cls.order_test = {
            "order_total": 0,
            "created_at": 2022 - 3 - 10,
        }
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
        cls.order = Order.objects.create(**cls.order_test, user=cls.user)
        cls.discount = Discount.objects.create(**cls.discount_test)
        cls.category = Category.objects.create(**cls.category_test)
        cls.product = Product.objects.create(
            **cls.product_test, discount_id=cls.discount.id, category_id=cls.category.id
        )
        cls.orderdetail = OrderDetails.objects.create(
            **cls.orderdetail_test, order=cls.order, product=cls.product
        )

    def test_orderdetail_fields(self):

        self.assertEqual(
            self.orderdetail.final_price,
            self.orderdetail_test["final_price"],
            "verificando field de final price",
        )
        self.assertEqual(
            self.orderdetail.quantity_in_order,
            self.orderdetail_test["quantity_in_order"],
            "verificando quantity_in_order",
        )

    def test_relation_with_user(self):

        self.assertIs(self.orderdetail.user, self.user, "verificando relação com user")
