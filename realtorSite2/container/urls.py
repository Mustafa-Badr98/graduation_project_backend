
from django.urls import path
from container.views import Index

urlpatterns = [
  
    path('',Index.as_view() ,name='home')
]
