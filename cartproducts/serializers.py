from rest_framework import serializers
import ipdb
from .models import Cartproducts
from products.serializers import ProductSerializer
from carts.models import Cart
from discounts.models import Discount

class CartProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cartproducts
        fields = "__all__"
        
        
    def create(self, validated_data):
        
        
        cartproduct_obj = Cartproducts.objects.filter(cart_id=validated_data['cart'], product_id=validated_data['product']).first()
        new_qtd = 0
        if cartproduct_obj:
            if validated_data.get('quantity'):
                cartproduct_obj.quantity += validated_data['quantity']
                new_qtd = validated_data['quantity']
                
            else:
                cartproduct_obj.quantity +=1
                new_qtd = 1
               
            cartproduct_obj.save()
            
        else:
            cartproduct_obj = Cartproducts.objects.create(**validated_data)
            new_qtd = validated_data.get('quantity') or 1


        cart_obj = Cart.objects.get(id=validated_data['cart'].id)
        discount_obj = Discount.objects.get(id=cartproduct_obj.product.discount_id)
        cart_obj.subtotal += cartproduct_obj.product.price*discount_obj.discount_percent*new_qtd
        cart_obj.save()
         
        return cartproduct_obj 

    
    

        
class ListCartProductsSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    class Meta:
        model = Cartproducts
        fields = ['id',"product","quantity", "productValue"]

