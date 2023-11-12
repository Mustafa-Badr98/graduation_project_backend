from django.urls import path,include

from comments.api.views import AddComment,DeleteComment

urlpatterns = [
	path('add_comment/',AddComment.as_view(),name="user_comment_add"),
	path('delete_comment/<int:comment_id>',DeleteComment.as_view(),name="user_comment_delete"),
   
]
