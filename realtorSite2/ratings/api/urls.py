from django.urls import path,include

from ratings.api.views import userRating,RatingIndex

urlpatterns = [
	path('rate/',userRating,name="user_rate"),
	path('allRatings/',RatingIndex.as_view(),name="rate_index"),
   
]
