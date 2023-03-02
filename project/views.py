from datetime import datetime
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


def home(request):
    response = render(request, 'Rateaurant/Home.html')
    return response


def NA(request):
    return HttpResponse('never gonna giv u up')
