# urls.py
from django.urls import path,include
from properties.api.views import index,property_resource,postAd,PropertyListFilteredAPIView,UserAddFavAd,IndexProperty,UserRemFavAd


urlpatterns = [
    path("postAd/", postAd, name="post_ad"),
    path('properties',IndexProperty.as_view(),name="properties.index"),
    path('properties/<int:id>',property_resource, name='property.api.resource'),
    path('properties/filtered/', PropertyListFilteredAPIView.as_view(), name='property-list-filtered'),
    path('property/AddFav/<int:id>',UserAddFavAd.as_view(),name="user_add_fav_AD"),
    path('property/RemFav/<int:id>',UserRemFavAd.as_view(),name="user_rem_fav_AD"),
    
]

