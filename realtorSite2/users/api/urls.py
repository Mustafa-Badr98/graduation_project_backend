# urls.py
from django.urls import path,include
# from properties.api.views import index,property_resource
from users.api.views import UsersIndex,RatingIndex,get_user_by_email
from . import views
urlpatterns = [
	path('ratings/',RatingIndex,name="ratings_index"),
    path('users/',UsersIndex,name="users_index"),
    path('user/<email>',get_user_by_email,name="get_user_by_id"),
    path('user/register', views.UserRegister.as_view(), name='register'),
	path('user/login', views.UserLogin2.as_view(), name='login'),
	path('user/logout', views.UserLogout.as_view(), name='logout'),
	path('user', views.UserView.as_view(), name='user'),
]
