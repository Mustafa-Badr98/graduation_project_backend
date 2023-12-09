from django.urls import path
from .views import OfferList, OfferDetail, AddOfferAPIView, GetPropertyOffersAPIView, RejectPropertyOffersAPIView, AcceptPropertyOffersAPIView
from .views import AdminDeleteOffersAPIView, GetOfferByID,SendDealLinkEmail
urlpatterns = [
    path('offers/', OfferList.as_view(), name='offer_list'),
    path('offers/<int:pk>/', OfferDetail.as_view(), name='offer_detail'),
    path('get_offer/<int:id>/', GetOfferByID.as_view(), name='get_offer_byID'),
    path('add_offer/', AddOfferAPIView.as_view(), name='add_offer'),
    path('send_deal_emil/<int:id>', SendDealLinkEmail.as_view(), name='send_email'),
    path('get_property_offers/<int:id>',
         GetPropertyOffersAPIView.as_view(), name='get_property_offers'),
    path('reject_offer/<int:id>',
         RejectPropertyOffersAPIView.as_view(), name='reject_offer'),
    path('accept_offer/<int:id>',
         AcceptPropertyOffersAPIView.as_view(), name='accept_offer'),
    path('admin_delete_offer/<int:id>',
         AdminDeleteOffersAPIView.as_view(), name='admin_delete_offer'),

]
