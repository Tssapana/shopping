from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import CartItem, Cart
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=User)
def add_to_cart(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(user=instance)
        Token.objects.create(user=instance)