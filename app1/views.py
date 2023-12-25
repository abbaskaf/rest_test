from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status, viewsets
from .serializers import ProfileSerializer, WorkSerializer, UserSerializer
from .models import Profile, Work
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import IsOwner


@api_view(['GET', 'POST'])
def ProfileView(request):
    if request.method == "GET":
        obj = Profile.objects.all()
        ser = ProfileSerializer(obj, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)
    if request.method == "POST":
        ser = ProfileSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_200_OK)
        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


class WorkViewsets(viewsets.ModelViewSet):
    search_fields = ('Name',)
    ordering_fields = '__all__'
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    http_method_names = ('get', 'post', 'put', 'delete')


@api_view(['POST'])
@permission_classes((AllowAny,))
def UserView(request):
    ser = UserSerializer(data=request.data)
    if ser.is_valid():
        ser.save()
        return Response(ser.data, status=status.HTTP_200_OK)
    else:
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes((IsAuthenticated, IsOwner))
def UserSingle(request):
    try:
        obj = User.objects.get(username=request.query_params['username'])
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    ser = UserSerializer(obj)
    return Response(ser.data, status=status.HTTP_200_OK)
