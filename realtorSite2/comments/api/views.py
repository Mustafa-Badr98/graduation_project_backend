
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import permissions, status
from users.models import NewUser
from comments.models import Comment
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from comments.api.serializers import CommentSerializer


class AddComment(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            # print(request.data)
            user = NewUser.objects.get(id=(request.data.get("user")))
            user2 = request.user
            content = request.data.get("content")

            # print(user)
            # print(user2)
            # print(content)

            comment_data = {
                'user': user,
                'commented_by': user2,
                'content': content
            }
            print(comment_data)
            # print(user.comments_on_user.all())

            comment = Comment.objects.create(**comment_data)
            serialized_comment = CommentSerializer(comment)
            # print(user.comments_on_user.all())
            # print(user.comments_given_by_user.all())

            return Response({'comment': serialized_comment.data}, status=status.HTTP_200_OK)

        except:
            return Response({'you have commented before'}, status=status.HTTP_200_OK)
