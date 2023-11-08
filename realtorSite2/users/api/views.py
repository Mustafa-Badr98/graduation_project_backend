from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ratings.models import Rating
from users.models import NewUser
from users.api.serializers import UserSerializer
from django.contrib.auth import get_user_model, login, logout, authenticate
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserRegisterSerializer, UserLoginSerializer, UserSerializer
from rest_framework import permissions, status
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from ratings.api.serializers import RatingSerializer
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


@api_view(['GET'])
@permission_classes([AllowAny])
def RatingIndex(request):

    if request.method == 'GET':
        user = NewUser.objects.get(id=11)

        # Create a new rating instance
        rating_data = {
            'user': user,
            'rated_by': user,  # You may set this to a specific user or keep it as None
            'rating': 5
        }

        # Create and save the Rating instance
        rating = Rating.objects.create(**rating_data)

        # Optionally, you can update the user's ratings field
        user.ratings.add(rating)

        return Response({'users'}, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def UsersIndex(request):
    if request.method == 'POST':
        pass
        serialized_user = UserSerializer(data=request.data)
        if serialized_user.is_valid():
            serialized_user.save()
            return Response({'user': serialized_user.data}, status=201)
        return Response({'errors': serialized_user.errors}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':

        users = NewUser.get_all_users()
        serialized_users = UserSerializer(users, many=True)

        return Response({'users': serialized_users.data}, status=status.HTTP_200_OK)

    else:
        return Response({"message": "This Method is Not Allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)





class UserReg(APIView):
        permission_classes = (permissions.AllowAny,)
        authentication_classes = ()
        def post(self, request):
            serialized_user = UserRegisterSerializer(data=request.data)
            if serialized_user.is_valid():
                print(serialized_user.validated_data)   
                serialized_user.save()
                return Response({'user': serialized_user.data}, status=status.HTTP_201_CREATED)
            return Response({'errors': serialized_user.errors}, status=status.HTTP_400_BAD_REQUEST)



class UserLogin2(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request):
        data = request.data
        user = authenticate(username=data['email'], password=data['password'])
        if user is not None:
            login(request, user)
            print(request.user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class UserView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response({'user': serializer.data}, status=status.HTTP_200_OK)


        
    



class UserLogout(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        token = request.headers.get('Authorization', '').split(' ')[1]
        user_token = Token.objects.get(key=token)
        user_token.delete()
 
        logout(request)
        return Response("logout succuss", status=status.HTTP_200_OK)


# @api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([AllowAny])
# def property_resource(request, id):
#     property = Property.get_specific_property(id)
#     if property and request.method == 'PUT':
#         serialized_property = PropertyModelSerializerPost(
#             data=request.data, instance=property)
#         if serialized_property.is_valid():
#             serialized_property.save()
#             return Response({'property': serialized_property.data}, status=200)
#         return Response({'errors': serialized_property.errors}, status=status.HTTP_400_BAD_REQUEST)

#     elif property and request.method == 'DELETE':
#         property.delete()
#         return Response({"message": "Deleted Successfully! "},
#                         status=status.HTTP_204_NO_CONTENT)

#     elif property and request.method == 'GET':
#         serialized_property = PropertyModelSerializerGet(property)
#         return Response({'data': serialized_property.data}, status=status.HTTP_200_OK)

#     else:
#         return Response({"message": "object not found , please reload the page"},
#                         status=status.HTTP_205_RESET_CONTENT)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_user_by_email(request, email):

    user = NewUser.get_specific_user(email)
    if user and request.method == 'GET':
        serialized_user = UserSerializer(user)
        return Response({'data': serialized_user.data}, status=status.HTTP_200_OK)

    else:
        return Response({"message": "object not found , please reload the page"},
                        status=status.HTTP_205_RESET_CONTENT)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_user_by_token(request, token):
    print(token)
    user_token = Token.objects.get(key=token)
    print(user_token.user)
    if user_token and request.method == 'GET':
        serialized_user = UserSerializer(user_token.user)
        return Response({'data': serialized_user.data}, status=status.HTTP_200_OK)

    else:
        return Response({"message": "object not found , please reload the page"},
                        status=status.HTTP_205_RESET_CONTENT)


class GetUserInSession(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        print(request.user)

        return Response("logout succuss", status=status.HTTP_200_OK)















# class UserRegister(APIView):
#     permission_classes = (permissions.AllowAny,)

#     def post(self, request):
#         clean_data = request.data
#         serializer = UserRegisterSerializer(data=clean_data)
#         if serializer.is_valid(raise_exception=True):
#             print(clean_data)
#             user = serializer.create(clean_data)
#             if user:
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)


# class UserLogin(APIView):
#     permission_classes = (permissions.AllowAny,)
#     authentication_classes = (SessionAuthentication,)

#     def post(self, request):
#         data = request.data
#         serializer = UserLoginSerializer(data=data)

#         if serializer.is_valid():
#             user = serializer.check_user(data)
#             print(user)
#             if (user):
#                 print("mustafa")
#                 login(request, user)
#                 return Response(serializer.data, status=status.HTTP_200_OK)
#             else:
#                 return Response("no user")

#         else:
#             print("hdddddddddddddddddddddsjsjd")
#             return Response({"message": "object not found , please reload the page"},
#                             status=status.HTTP_205_RESET_CONTENT)

