from django.urls import path
from .views import OfferList, OfferDetail, AddOfferAPIView, GetPropertyOffersAPIView, RejectPropertyOffersAPIView, AcceptPropertyOffersAPIView

urlpatterns = [
    path('offers/', OfferList.as_view(), name='offer_list'),
    path('offers/<int:pk>/', OfferDetail.as_view(), name='offer_detail'),
    path('add_offer/', AddOfferAPIView.as_view(), name='add_offer'),
    path('get_property_offers/<int:id>',
         GetPropertyOffersAPIView.as_view(), name='get_property_offers'),
    path('reject_offer/<int:id>',
         RejectPropertyOffersAPIView.as_view(), name='reject_offer'),
    path('accept_offer/<int:id>',
         AcceptPropertyOffersAPIView.as_view(), name='accept_offer'),


]
