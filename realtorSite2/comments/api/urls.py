from django.urls import path,include

from comments.api.views import addComment

urlpatterns = [
	path('add_comment/',addComment,name="user_comment"),
   
]
