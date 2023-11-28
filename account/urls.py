from django.urls import path, include
from .views import UserLoginView, UserLogoutAPIView, UserSignupModelViewset
from rest_framework.routers import DefaultRouter


app_name= 'account'

router= DefaultRouter()

router.register(r'sign-up', UserSignupModelViewset, basename= 'sign-up')

urlpatterns = [
    path('login/', UserLoginView.as_view(), name= 'login'),
    path('logout/', UserLogoutAPIView.as_view(), name= 'logout'),
    path('', include(router.urls))
   
]