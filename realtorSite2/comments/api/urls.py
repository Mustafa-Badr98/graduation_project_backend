from django.urls import path,include

from comments.api.views import AddComment,DeleteComment,CommentIndex,AdminDeleteComment

urlpatterns = [
	path('comments/',CommentIndex.as_view(),name="comment_index"),
	path('add_comment/',AddComment.as_view(),name="user_comment_add"),
	path('delete_comment/<int:comment_id>',DeleteComment.as_view(),name="user_comment_delete"),
	path('delete_comment/admin/<int:comment_id>',AdminDeleteComment.as_view(),name="user_comment_delete_admin"),
   
]
