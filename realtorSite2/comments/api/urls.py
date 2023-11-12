from django.urls import path,include

from comments.api.views import AddComment

urlpatterns = [
	path('add_comment/',AddComment.as_view(),name="user_comment"),
   
]
