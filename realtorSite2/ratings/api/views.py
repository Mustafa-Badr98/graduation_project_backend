
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from users.models import NewUser
from ratings.models import Rating
from rest_framework import status
from rest_framework.response import Response





@api_view(['POST'])
@permission_classes([AllowAny])
def userRating(request):

    if request.method == 'POST':
        try:
            user=NewUser.objects.get(id=11)
            user2=NewUser.objects.get(id=14)
                
            rating_data = {
                'user': user,
                'rated_by': user2,  # You may set this to a specific user or keep it as None
                'rating': 2
            }

            
            rating = Rating.objects.create(**rating_data)

            # Optionally, you can update the user's ratings field
            user.ratings.add(rating)
            
            return Response({'users'}, status=status.HTTP_200_OK)

        except:
            return Response({'you have rated before'}, status=status.HTTP_200_OK)