# urls.py
from django.urls import path,include
from users.views import UserCreateView,UserLoginView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('create/', UserCreateView.as_view(), name='create-user'),
    path('login/', UserLoginView.as_view(), name='user-login'),
]
