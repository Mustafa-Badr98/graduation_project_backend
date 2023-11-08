# urls.py
from django.urls import path,include
from properties.api.views import index,property_resource,postAd,PropertyListFilteredAPIView,addPropertyImage

urlpatterns = [
    path("postAd/", postAd, name="post_ad"),
    path('properties',index,name="properties.index"),
    path('properties/<int:id>',property_resource, name='property.api.resource'),
    path('properties/filtered/', PropertyListFilteredAPIView.as_view(), name='property-list-filtered'),
    path('addImage/',addPropertyImage,name="add_image")
]

