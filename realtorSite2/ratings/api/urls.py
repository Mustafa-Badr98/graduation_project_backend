from django.urls import path,include

from ratings.api.views import userRating

urlpatterns = [
	path('rate/',userRating,name="user_rate"),
   
]
