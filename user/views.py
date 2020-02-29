from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth.models import User
import json


# Create your views here.

@api_view(['POST'])
def UserRegisterView(request):
	data = json.loads(request.body)
	username = data['username']
	email = data['email']
	password = data['password']
	user = User.objects.create_user(username, email, password)
	user.save()
	return 




