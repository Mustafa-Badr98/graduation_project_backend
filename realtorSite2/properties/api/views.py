from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from properties.models import Property
from properties.api.serializers import PropertySerializer,PropertyModelSerializerPost
from properties.api.serializer2 import PropertyModelSerializerGet
from users.models import NewUser
from rest_framework import permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes




@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def postAd(request):

    if request.method == 'POST':
        user=request.user
        print(user)
        serialized_property = PropertyModelSerializerPost(data=request.data)
        if serialized_property.is_valid():
            serialized_property.validated_data['seller'] = user
            print(serialized_property.validated_data)
            serialized_property.save()
            return Response({'properties': serialized_property.data}, status=201)
        return Response({'errors': serialized_property.errors}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@permission_classes([AllowAny])
def index(request):

    if request.method == 'GET':
        properties = Property.get_all_properties()
        serialized_properties = PropertyModelSerializerGet(properties, many=True)
        return Response({'properties': serialized_properties.data})



@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
def property_resource(request, id):
    property = Property.get_specific_property(id)
    if property and request.method == 'PUT':
        serialized_property = PropertyModelSerializerPost(
            data=request.data, instance=property)
        if serialized_property.is_valid():
            serialized_property.save()
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
