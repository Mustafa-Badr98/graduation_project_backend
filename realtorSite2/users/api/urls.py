# urls.py
from django.urls import path,include
# from properties.api.views import index,property_resource
from users.api.views import UsersIndex
urlpatterns = [
    # path('properties',index,name="properties_index"),
    # path('properties/<int:id>',property_resource, name='property.api.resource'),
    path('users/',UsersIndex,name="users_index")
]
