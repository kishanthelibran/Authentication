from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import UserModel
from django.http import HttpResponse
from django.core import serializers
from .serializer import UserSerializer
from rest_framework import status

# Create your views here.


# class RegisterUser(APIView):

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def RegisterUser(request):
    serializers = UserSerializer(data=request.data)
    serializers.is_valid(raise_exception=True)
    serializers.save()

    '''name = request.data['name']
    city = request.data['city']
    salary = request.data['salary']
    dept = request.data['dept']
    role = request.data['role']
    user = UserModel(name=name, city=city,
                     dept_id=dept, role_id=role, salary=salary)
    user.save()'''

    return Response(serializers.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def getData(request):
    salary = request.data['salary']

    user = UserModel.objects.filter(salary__gte=salary)

    data = serializers.serialize("json", user)

    return Response(data)
