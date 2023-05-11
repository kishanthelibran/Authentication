from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserModel
from django.http import HttpResponse

# Create your views here.


class RegisterUser(APIView):
    def get(self, request):
        name = request.data['name']
        city = request.data['city']
        salary = request.data['salary']
        dept = request.data['dept']
        role = request.data['role']
        user = UserModel(name=name, city=city,
                         dept_id=dept, role_id=role, salary=salary)
        user.save()
        return Response('user successfully registered')
