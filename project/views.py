from datetime import datetime
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


def home(request):
    response = render(request, 'Rateaurant/Home.html')
    return response


def categories(request):
    response = render(request, 'Rateaurant/Categories.html')
    return response


def register(request):
    response = render(request, 'Rateaurant/Register.html')
    return response


def login(request):
    response = render(request, 'Rateaurant/Login.html')
    return response


def add_a_restaurant(request):
    response = render(request, 'Rateaurant/AddARestaurant.html')
    return response


def na(request):
    return HttpResponse('never gonna giv u up')
