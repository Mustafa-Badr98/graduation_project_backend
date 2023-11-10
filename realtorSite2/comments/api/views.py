
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from users.models import NewUser
from comments.models import Comment
from rest_framework import status
from rest_framework.response import Response


@api_view(['POST'])
@permission_classes([AllowAny])
def addComment(request):

    if request.method == 'POST':
        try:
            user = NewUser.objects.get(id=11)
            user2 = NewUser.objects.get(id=40)

            comment_data = {
                'user': user,
                'commented_by': user2,
                'content': "this came from postman"
            }
            print(user.comments_on_user.all())

            comment = Comment.objects.create(**comment_data)

            print(user.comments_on_user.all())
            print(user.comments_given_by_user.all())

            return Response({'ok'}, status=status.HTTP_200_OK)

        except:
            return Response({'you have commented before'}, status=status.HTTP_200_OK)
