from django.urls import path
from .views import OfferList, OfferDetail

urlpatterns = [
    path('offers/', OfferList.as_view(), name='offer_list'),
    path('offers/<int:pk>/', OfferDetail.as_view(), name='offer_detail'),
]
