
from rest_framework import serializers
from comments.models import Comment
from users.api.serializers3 import UserCommentSerializer


class CommentSerializer(serializers.ModelSerializer):
    commented_by = UserCommentSerializer(read_only=True)
    user = UserCommentSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
