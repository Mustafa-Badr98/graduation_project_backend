# urls.py
from django.urls import path,include
from properties.api.views import index,property_resource,postAd

urlpatterns = [
    path("postAd/", postAd, name="post_ad"),
    path('properties',index,name="properties.index"),
    path('properties/<int:id>',property_resource, name='property.api.resource'),
]
