# urls.py
from django.urls import path,include
# from properties.api.views import index,property_resource
from users.api.views import UsersIndex,RatingIndex
from . import views
urlpatterns = [
	path('ratings/',RatingIndex,name="ratings_index"),
    path('users/',UsersIndex,name="users_index"),
    path('user/register', views.UserRegister.as_view(), name='register'),
	path('user/login', views.UserLogin2.as_view(), name='login'),
	path('user/logout', views.UserLogout.as_view(), name='logout'),
	path('user', views.UserView.as_view(), name='user'),
]
