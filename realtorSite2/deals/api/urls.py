from django.urls import path
from .views import DealsListAPIView,GetDealByIdAPIView,AddDealAPIView

urlpatterns = [
    path('deals/', DealsListAPIView.as_view(), name='deals_list'),
    path('deals/<int:id>', GetDealByIdAPIView.as_view(), name='deal_by_id'),
    path('add_deal/', AddDealAPIView.as_view(), name='add_deal'),
    # path('offers/<int:pk>/', OfferDetail.as_view(), name='offer_detail'),
]
