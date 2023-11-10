from rest_framework import generics
from rest_framework import permissions
from offers.models import Offer
from .serializers import OfferSerializer


class OfferList(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

class OfferDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
