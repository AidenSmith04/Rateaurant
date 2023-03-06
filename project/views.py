from datetime import datetime
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from project.models import Restaurant, Owner
from project.forms import CustomerForm, OwnerForm, RestaurantForm, UserForm, Categories
from Populate_Rateaurant import generateID


def home(request):
    response = render(request, 'Rateaurant/Home.html')
    return response


def categories(request):
    response = render(request, 'Rateaurant/Categories.html', context={'categories': Categories})
    return response


def show_category(request, category_name):
    context_dict = {}
    try:
        venues = Restaurant.objects.filter(category=category_name)
        context_dict['venues'] = venues

    except Restaurant.DoesNotExist:
        context_dict['venues'] = None

    return render(request, 'Rateaurant/Category.html', context=context_dict)


def show_venue(request, category_name, venue_id):
    context_dict = {}
    try:

        venue = Restaurant.objects.get(restaurant_ID=venue_id)
        context_dict['venue'] = venue

    except Restaurant.DoesNotExist:
        context_dict['venue'] = None

    return render(request, 'Rateaurant/Restaurant.html', context=context_dict)


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
        if not registered:
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
    if request.method == 'POST':
        restaurant_form = RestaurantForm(request.POST)

        if restaurant_form.is_valid():
            restaurant = restaurant_form.save(commit=False)
            restaurant.restaurant_ID = generateID()
            restaurant.owner_ID = Owner.objects.get(user=request.user).owner_ID
            restaurant.save()
            return redirect(reverse('Rateaurant:home'))
    else:
        restaurant_form = RestaurantForm()

    return render(request, 'Rateaurant/AddARestaurant.html', context={'restaurant_form': restaurant_form})


def user_logout(request):
    logout(request)
    return redirect(reverse('Rateaurant:home'))
