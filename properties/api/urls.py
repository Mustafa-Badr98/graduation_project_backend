# urls.py
from django.urls import path,include
from properties.api.views import index,property_resource,postAd,PropertyListFilteredAPIView,UserAddFavAd,AdminIndexProperty,IndexProperty,UserRemFavAd,AdminPropertyListFilteredAPIView


urlpatterns = [
    path("postAd/", postAd, name="post_ad"),
    path('properties',IndexProperty.as_view(),name="properties.index"),
    path('properties/admin',AdminIndexProperty.as_view(),name="properties_index_admin"),
    path('properties/<int:id>',property_resource, name='property.api.resource'),
    path('properties/filtered/', PropertyListFilteredAPIView.as_view(), name='property_list_filtered'),
    path('properties/admin/filtered/', AdminPropertyListFilteredAPIView.as_view(), name='property_list_filtered_admin'),
    path('property/AddFav/<int:id>',UserAddFavAd.as_view(),name="user_add_fav_AD"),
    path('property/RemFav/<int:id>',UserRemFavAd.as_view(),name="user_rem_fav_AD"),
    
]

