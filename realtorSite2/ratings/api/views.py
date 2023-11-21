
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from users.models import NewUser
from ratings.models import Rating
from rest_framework import status
from rest_framework.response import Response
from django.db.models import Q
from ratings.api.serializers import RatingSerializer
from rest_framework import permissions


class RatingIndex(APIView):
    permission_classes = [AllowAny]

    def get(self, request):

        ratings = Rating.objects.all()
        serialized_ratings = RatingSerializer(
            ratings, many=True)
        return Response({'ratings': serialized_ratings.data})


@api_view(['POST'])
@permission_classes([AllowAny])
def userRating(request):

    if request.method == 'POST':
        try:
            user = NewUser.objects.get(id=request.data.get('user_id'))
            rated_by = NewUser.objects.get(id=request.data.get('rated_by_id'))
            rate = request.data.get('rate')
            existing_rating = Rating.objects.filter(
                Q(user=user) & Q(rated_by=rated_by)
            ).first()

            if existing_rating:
                # Update the existing rating
                print(existing_rating.rating)
                existing_rating.rating = rate
                existing_rating.save()
                print(existing_rating.rating)

            else:
                # Create a new rating
                rating_data = {
                    'user': user,
                    'rated_by': rated_by,
                    'rating': rate
                }
                rating = Rating.objects.create(**rating_data)

                # Optionally, you can update the user's ratings field
                user.ratings.add(rating)

            return Response({'Rating Created'}, status=status.HTTP_200_OK)

        except:
            return Response({'you have rated before'}, status=status.HTTP_200_OK)


class AdminDeleteRatingAPIView(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def delete(self, request, id):
        rating = Rating.objects.get(id=id)
        print(rating)
        rating.delete()
        return Response('Rating Deleted', status=200)
