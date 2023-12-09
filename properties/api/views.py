from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from properties.models import Property, PropertyImage
from properties.api.serializers import PropertySerializer, PropertyModelSerializerPost
from users.api.serializers import UserSerializer
from properties.api.serializer2 import PropertyModelSerializerGet
from users.models import NewUser
from rest_framework import permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from properties.filters import PropertyFilter,PropertySearchFilter
from urllib.parse import quote
from django.core.exceptions import ObjectDoesNotExist


@api_view(['POST'])
@permission_classes([AllowAny])
def addPropertyImage(request):

    if request.method == 'POST':
        property = Property.objects.get(id=45)
        print(request.FILES.get("image"))
        PropertyImage.objects.create(
            property=property, image=request.FILES.get("image"))
        # property.images.add()
        # serialized_properties = PropertyModelSerializerGet(properties, many=True)
        return Response({'ok'})


@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def postAd(request):

    if request.method == 'POST':
        user = request.user
        # print(user)
        print(request.FILES)
        serialized_property = PropertyModelSerializerPost(data=request.data)
        if serialized_property.is_valid():
            serialized_property.validated_data['seller'] = user
            property_instance = serialized_property.save()
            # print(property_instance.id)
            created_property = Property.objects.get(id=property_instance.id)
            # print(created_property)

            images_data = request.FILES.getlist('images')
            print(images_data)
            for image_data in images_data:
                PropertyImage.objects.create(
                    property=created_property, image=image_data)

            # print(property_instance.images.all())
            return Response({'properties': serialized_property.data}, status=201)
        return Response({'errors': serialized_property.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([AllowAny])
def index(request):

    if request.method == 'GET':
        properties = Property.get_sold_properties()
        serialized_properties = PropertyModelSerializerGet(
            properties, many=True)
        return Response({'properties': serialized_properties.data})


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
def property_resource(request, id):
    property = Property.get_specific_property(id)
    print(property)
    if property and request.method == 'PUT':
        serialized_property = PropertyModelSerializerPost(
            data=request.data, instance=property)
        if serialized_property.is_valid():
            serialized_property.save()

            property = Property.get_specific_property(id)

            try:
                existing_images = PropertyImage.objects.filter(
                    property=property)
                existing_images.delete()
            except ObjectDoesNotExist:
                pass  # No existing images, do nothing

            images_data = request.FILES.getlist('images')
            print(images_data)
            for image_data in images_data:
                PropertyImage.objects.create(
                    property=property, image=image_data)

            return Response({'property': serialized_property.data}, status=200)
        return Response({'errors': serialized_property.errors}, status=status.HTTP_400_BAD_REQUEST)

    elif property and request.method == 'DELETE':
      
        property.delete()
        return Response({"message": "Deleted Successfully! "},
                        status=status.HTTP_204_NO_CONTENT)

    elif property and request.method == 'GET':
        serialized_property = PropertyModelSerializerGet(property)
        return Response({'data': serialized_property.data}, status=status.HTTP_200_OK)

    else:
        return Response({"message": "object not found , please reload the page"},
                        status=status.HTTP_205_RESET_CONTENT)


class PropertyListFilteredAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        queryset = Property.get_live_properties()

        print(request.query_params)

        filtered_queryset = PropertyFilter(
            request.query_params, queryset=queryset).qs
        print(filtered_queryset.query)
        # print(request.query_params)
        serializer = PropertyModelSerializerGet(filtered_queryset, many=True)
        return Response(serializer.data)


class IndexProperty(APIView):
    permission_classes = [AllowAny]

    def get(self, request):

        properties = Property.get_live_properties()
        serialized_properties = PropertyModelSerializerGet(
            properties, many=True)
        return Response({'properties': serialized_properties.data})


class AdminIndexProperty(APIView):
    permission_classes = [AllowAny]

    def get(self, request):

        properties = Property.get_all_properties()
        serialized_properties = PropertyModelSerializerGet(
            properties, many=True)
        return Response({'properties': serialized_properties.data})
    
    
class AdminPropertyListFilteredAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        queryset = Property.objects.all()

        print(request.query_params)

        filtered_queryset = PropertySearchFilter(
            request.query_params, queryset=queryset).qs
        print(filtered_queryset.query)
        # print(request.query_params)
        serializer = PropertyModelSerializerGet(filtered_queryset, many=True)
        return Response(serializer.data)    
    
class UserAddFavAd(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, id):
        property = Property.get_specific_property(id)

        if property:
            user = request.user
            user.favorites.add(property)
            user.save()
            # print(user)
            # print(request.user.favorites.all())
            serialized_user = UserSerializer(user)
            return Response({'user': serialized_user.data}, status=status.HTTP_200_OK)

        else:
            return Response({"message": "Object not found. Please reload the page."},
                            status=status.HTTP_205_RESET_CONTENT)


class UserRemFavAd(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, id):
        property = Property.get_specific_property(id)

        if property:
            user = request.user
            user.favorites.remove(property)
            user.save()
            # print(user)
            # print(request.user.favorites.all())
            serialized_user = UserSerializer(user)
            return Response({'user': serialized_user.data}, status=status.HTTP_200_OK)

        else:
            return Response({"message": "Object not found. Please reload the page."},
                            status=status.HTTP_205_RESET_CONTENT)
