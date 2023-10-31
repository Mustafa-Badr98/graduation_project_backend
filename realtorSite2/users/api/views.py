from rest_framework.decorators import  api_view
from rest_framework.response import  Response
from rest_framework import status

from users.models import NewUser
from users.api.serializers import UserSerializer


@api_view(['GET', 'POST'])
def UsersIndex(request):
    if request.method == 'POST':
        pass
        serialized_user =UserSerializer(data=request.data)
        if serialized_user.is_valid():
            serialized_user.save()
            return Response({'user': serialized_user.data}, status=201)
        return Response({'errors': serialized_user.errors}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
   
        users= NewUser.get_all_users()
        serialized_users= UserSerializer(users, many=True)
        return Response({'users':serialized_users.data} ,status=status.HTTP_200_OK)

    
    else:
        return Response({"message":"This Method is Not Allowed."},status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    
    
# @api_view(['GET', 'PUT', 'DELETE'])
# def property_resource(request, id):
#     property = Properties.get_specific_property(id)
#     if property and request.method == 'PUT':
#         serialized_property = PropertySerializer(data=request.data, instance=property)
#         if serialized_property.is_valid():
#             serialized_property.save()
#             return Response({'property': serialized_property.data}, status=200)
#         return Response({'errors': serialized_property.errors}, status=status.HTTP_400_BAD_REQUEST)

#     elif property and request.method == 'DELETE':
#         property.delete()
#         return Response({"message": "Deleted Successfully! "},
#                         status=status.HTTP_204_NO_CONTENT)

#     elif property and request.method == 'GET':
#         serialized_property = PropertySerializer(property)
#         return Response({'data': serialized_property.data}, status=status.HTTP_200_OK)

#     else:
#         return  Response({"message":"object not found , please reload the page"},
#                          status=status.HTTP_205_RESET_CONTENT)

    