# Generated by Django 4.1.1 on 2022-09-14 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cartproducts", "0004_remove_cartproducts_productvalue"),
    ]

    operations = [
        migrations.RenameField(
            model_name="cartproducts",
            old_name="quantity",
            new_name="quantity_in_cart",
        ),
    ]
