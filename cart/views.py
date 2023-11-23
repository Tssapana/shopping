
from rest_framework.viewsets import ModelViewSet
from .models import CartItem
from .serilaizers import CartItemSerializer

# Create your views here.

class CartModelViewSet(ModelViewSet):
    serializer_class = CartItemSerializer

    def  get_queryset(self):
        qs= CartItem.objects.filter(user= self.request.user)
        return qs
    

