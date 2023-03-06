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

        if user_form.is_valid() and (customer_form.is_valid() or owner_form.is_valid()):
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()
            login(request, user)

            if customer_form.is_valid():
                customer = customer_form.save(commit=False)
                customer.customer_ID = generateID()
                customer.user = user
                customer.save()

                registered = True
            elif owner_form.is_valid():
                owner = owner_form.save(commit=False)
                owner.owner_ID = generateID()
                owner.user = user
                owner.save()

                registered = True
        else:
            print(user_form.errors, customer_form.errors, owner_form.errors)
    else:
        user_form = UserForm()
        customer_form = CustomerForm()
        owner_form = OwnerForm()

    context = {
        'user_form': user_form,
        'customer_form': customer_form,
        'owner_form': owner_form,
        'registered': registered
    }

    return render(request, 'Rateaurant/Register.html', context=context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('Rateaurant:home'))
            else:
                return HttpResponse("Your Rateaurant account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'Rateaurant/Login.html')


@login_required()
def add_a_restaurant(request):
    response = render(request, 'Rateaurant/AddARestaurant.html')
    return response


def user_logout(request):
    logout(request)
    return redirect(reverse('Rateaurant:home'))
