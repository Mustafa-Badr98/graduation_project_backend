# urls.py
from django.urls import path,include
# from properties.api.views import index,property_resource
from users.api.views import UsersIndex,RatingIndex,get_user_by_email,get_user_by_token,UserReg,user_resource,UserListFilteredAPIView

from . import views
urlpatterns = [
	path('ratings/',RatingIndex,name="ratings_index"),
    path('users/',UsersIndex,name="users_index"),
    path('users/resources/<int:id>',user_resource,name="users_resources"),
    path('user/register', UserReg.as_view(), name='register'),
	path('user/login', views.UserLogin2.as_view(), name='login'),
	path('user/logout', views.UserLogout.as_view(), name='logout'),
	path('user', views.UserView.as_view(), name='user'),
	path('user/edit', views.EditUserView.as_view(), name='user_edit'),
	path('user/delete', views.DeleteUserView.as_view(), name='user_delete'),
    path('user/email/<email>',get_user_by_email,name="get_user_by_email"),
    path('user/token/<token>',get_user_by_token,name="get_user_by_token"),
	path('user/inSession', views.GetUserInSession.as_view(), name='user_in_session'),
	path('filtered_users/', views.UserListFilteredAPIView.as_view(), name='filtered_users'),
    
 
]
