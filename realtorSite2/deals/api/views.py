from .serializers import DealSerializer
from deals.models import Deal
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models import NewUser
from properties.models import Property


class DealsListAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        deals = Deal.objects.all()
        serialized_deals = DealSerializer(deals, many=True)

        return Response({'Deals': serialized_deals.data}, status=200)


class GetDealByIdAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, id):
        deal = Deal.objects.get(id=id)
        serialized_deal = DealSerializer(deal)

        return Response({'Deal': serialized_deal.data}, status=200)


class AddDealAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        print(request.data)
        seller = NewUser.objects.get(id=(request.data.get("seller_id")))
        buyer = NewUser.objects.get(id=(request.data.get("buyer_id")))
        property = Property.objects.get(id=(request.data.get("property_id")))
        price = request.data.get("price")

        deal_data = {
            'seller': seller,
            'buyer': buyer,
            'property': property,
            'price': price,
        }

        deal = Deal.objects.create(**deal_data)
        serialized_deal = DealSerializer(deal)

        return Response({'Deal': serialized_deal.data}, status=200)



