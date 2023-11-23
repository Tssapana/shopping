from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from product.models import Product

User= get_user_model()

# Create your models here.

class BaseModel(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    updated=models.DateTimeField(auto_now=True)
    created= models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract= True

class CartItem(BaseModel):
    product= models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity= models.PositiveBigIntegerField(default=1)

    def __str__ (self):
        return f'{self.product.name} is added to cart.'
    
    def total_price(self):
        total = self.product.price * self.quantity
        return total
    
    
# class Carts(BaseModel):
#     products=models.ForeignKey(CartItem, on_delete=models.CASCADE,
#                                related_name='carts')
    


