from datetime import datetime
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db.models import Avg, F
from project.models import Restaurant, Owner, Ratings
from project.forms import CustomerForm, OwnerForm, RestaurantForm, UserForm, Categories, OwnershipForm
from Populate_Rateaurant import generateID

rating_types = ['food_Rating', 'service_Rating', 'atmosphere_Rating', 'price_Rating']


def home(request):
    means = Ratings.objects.annotate(
        avg=(F('food_Rating') + F('service_Rating') + F('atmosphere_Rating') + F('price_Rating')) / 4)

    context_dict = {}
    top_venues = [x for x in means.order_by('-avg').values('rest_id', 'avg')]

    for i in range(0, 10):
        query = Restaurant.objects.get(restaurant_ID=top_venues[i]['rest_id'])
        top_venues[i]['name'] = query.name
        top_venues[i]['category'] = query.category

    context_dict = {'top_venues': top_venues}

    response = render(request, 'Rateaurant/Home.html', context=context_dict)
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

        for rating_type in rating_types:
            context_dict[rating_type] = Ratings.objects.filter(rest_id=venue_id).aggregate(Avg(rating_type))[
                rating_type + '__avg']

    except Restaurant.DoesNotExist:
        context_dict['venue'] = None

    return render(request, 'Rateaurant/Restaurant.html', context=context_dict)


def register(request):
    registered = False

    if request.method == 'POST':
        as_owner = request.POST.get('as_owner')
        email = request.POST.get('email')
        user_form = UserForm(request.POST)
        customer_form = CustomerForm(request.POST)
        owner_form = OwnerForm(request.POST)

        if user_form.is_valid() and customer_form.is_valid() and owner_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()
            login(request, user)
            if as_owner:
                owner = owner_form.save(commit=False)
                owner.owner_ID = generateID()
                owner.email = email
                owner.user = user
                owner.save()
            else:
                customer = customer_form.save(commit=False)
                customer.customer_ID = generateID()
                customer.email = email
                customer.user = user
                customer.save()
            registered = True
        if not registered:
            print(user_form.errors, customer_form.errors, owner_form.errors)
    else:
        user_form = UserForm()
        customer_form = CustomerForm()
        owner_form = OwnerForm()

    context = {
        'user_form': user_form,
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
        ownership_form = OwnershipForm(request.POST)

        if restaurant_form.is_valid() and ownership_form.is_valid():
            restaurant_id = generateID()

            restaurant = restaurant_form.save(commit=False)
            restaurant.restaurant_ID = restaurant_id
            print(request.FILES)
            if 'picture' in request.FILES:
                print('mogus')
                restaurant.picture = request.FILES['picture']

            restaurant.save()

            ownership = ownership_form.save(commit=False)
            ownership.restaurant_ID = restaurant
            ownership.owner_ID = Owner.objects.get(user=request.user)  # Owner.objects.get(user=request.user).owner_ID
            ownership.save()

            return redirect(reverse('Rateaurant:home'))
        else:
            print(restaurant_form.errors, ownership_form.errors)
    else:
        restaurant_form = RestaurantForm()

    return render(request, 'Rateaurant/AddARestaurant.html', context={'restaurant_form': restaurant_form})


def user_logout(request):
    logout(request)
    return redirect(reverse('Rateaurant:home'))
