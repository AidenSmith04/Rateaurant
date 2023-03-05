from datetime import datetime
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from project.models import Restaurant
from project.forms import CustomerForm, OwnerForm, RestaurantForm, UserForm
from Populate_Rateaurant import generateID


def home(request):
    response = render(request, 'Rateaurant/Home.html')
    return response


def categories(request):
    response = render(request, 'Rateaurant/Categories.html')
    return response


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        customer_form = CustomerForm(request.POST)
        owner_form = OwnerForm(request.POST)

        if customer_form.is_valid():
            customer = customer_form.save(commit=False)
            customer.customer_ID = generateID()
            login(request.P)
            registered = True
        elif owner_form.is_valid():
            owner = owner_form.save(commit=False)
            owner.owner_ID = generateID()
            owner.save()

            registered = True
        else:
            print(customer_form.errors, owner_form.errors)
    else:
        customer_form = CustomerForm()
        owner_form = OwnerForm()

    context = {'customer_form': customer_form, 'owner_form': owner_form, 'registered': registered}
    return render(request, 'Rateaurant/Register.html', context=context)


def login(request):
    response = render(request, 'Rateaurant/Login.html')
    return response


@login_required()
def add_a_restaurant(request):
    response = render(request, 'Rateaurant/AddARestaurant.html')
    return response


def na(request):
    return HttpResponse('never gonna giv u up')
