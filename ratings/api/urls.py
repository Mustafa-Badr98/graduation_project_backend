from django.urls import path, include

from ratings.api.views import userRating, RatingIndex, AdminDeleteRatingAPIView

urlpatterns = [
    path('rate/', userRating, name="user_rate"),
    path('allRatings/', RatingIndex.as_view(), name="rate_index"),
    path('rating/admin/delete/<int:id>',
         AdminDeleteRatingAPIView.as_view(), name="rate_admin_delete"),


]
