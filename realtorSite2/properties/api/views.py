from rest_framework.decorators import  api_view
from rest_framework.response import  Response
from rest_framework import status
from properties.models import Properties
from properties.api.serializers import PropertySerializer



@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'POST':
        # property = property.objects.create(name=request.data['name'],
        # email=request.data['email'],grade=request.data['grade'],image=request.data['image'])
        # property.save()
        serialized_property =PropertySerializer(data=request.data)
        if serialized_property.is_valid():
            serialized_property.save()
            return Response({'properties': serialized_property.data}, status=201)
        return Response({'errors': serialized_property.errors}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        # 1- get all objects
        properties= Properties.get_all_properties()
        serialized_properties= PropertySerializer(properties, many=True)

        return Response({'properties':serialized_properties.data})

    
@api_view(['GET', 'PUT', 'DELETE'])
def property_resource(request, id):
    property = Properties.get_specific_property(id)
    if property and request.method == 'PUT':
        serialized_property = PropertySerializer(data=request.data, instance=property)
        if serialized_property.is_valid():
            serialized_property.save()
            return Response({'property': serialized_property.data}, status=200)
        return Response({'errors': serialized_property.errors}, status=status.HTTP_400_BAD_REQUEST)

    elif property and request.method == 'DELETE':
        property.delete()
        return Response({"message": "Deleted Successfully! "},
                        status=status.HTTP_204_NO_CONTENT)

    elif property and request.method == 'GET':
        serialized_property = PropertySerializer(property)
        return Response({'data': serialized_property.data}, status=status.HTTP_200_OK)

    else:
        return  Response({"message":"object not found , please reload the page"},
                         status=status.HTTP_205_RESET_CONTENT)

    