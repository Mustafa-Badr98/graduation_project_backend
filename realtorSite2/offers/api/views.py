from rest_framework import generics
from rest_framework import permissions
from offers.models import Offer
from .serializers import OfferSerializer
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from properties.models import Property
from users.models import NewUser
from deals.models import Deal
from deals.api.serializers import DealSerializer
from django.core.mail import send_mail


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


class AddOfferAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        print(request.data)
        print(request.user)
        offer_user = request.user
        property = Property.objects.get(id=(request.data.get("property_id")))
        offer_price = request.data.get("price")
        print(property)
        offer_data = {
            'user': offer_user,
            'property': property,
            'price': offer_price,
        }

        offer = Offer.objects.create(**offer_data)
        serialized_offer = OfferSerializer(offer)

        return Response({'Offer': serialized_offer.data}, status=200)


class GetPropertyOffersAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, id):

        print(request.user)
        property = Property.objects.get(id=id)
        print(property)

        offers = property.offer_property.all()
        print(offers)
        serialized_offers = OfferSerializer(offers, many=True)

        return Response({'offers': serialized_offers.data}, status=200)


class RejectPropertyOffersAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, id):
        rejected_offer = Offer.objects.get(id=id)
        print(rejected_offer)
        rejected_offer.delete()
        return Response('Offer Rejected', status=200)


class AcceptPropertyOffersAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, id):
        accepted_offer = Offer.objects.get(id=id)

        deal_data = {
            'seller': request.user,
            'buyer': accepted_offer.user,
            'property': accepted_offer.property,
            'price': accepted_offer.price,
        }

        deal = Deal.objects.create(**deal_data)

        sold_property = accepted_offer.property
        sold_property.state = "sold"
        sold_property.save()

        all_other_offers = Offer.objects.filter(property=sold_property)
        all_other_offers.delete()

        users_favoriting_property = NewUser.objects.filter(
            favorites=sold_property)
        print(f'users are  : {users_favoriting_property}')

        for user in users_favoriting_property:
            user.favorites.remove(sold_property)

        serialized_deal = DealSerializer(deal)

        subject = 'About your Offer'
        message = (
            f"Dear User {accepted_offer.user.user_name},\n\n"
            "Congratulations! We are delighted to inform you that your offer has been accepted, "
            "and the deal is now complete. This is a significant milestone, and we appreciate your "
            "engagement throughout the process.\n\n"
            "If you have any questions or need further assistance, feel free to reach out. "
            "Thank you for choosing our platform.\n\n"
            "Best regards,\nThe [Your Company] Team"
        )
        from_email = 'mustafa.rm.badr@gmail.com'
        recipient_list = ['mustafabadrwork1998@gmail.com']

        send_mail(subject, message, from_email,
                  recipient_list, fail_silently=False)

        return Response({"deal": serialized_deal.data}, status=200)
