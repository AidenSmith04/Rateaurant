from django.test import TestCase
from django.urls import reverse
from django.test.client import Client

from Populate_Rateaurant import add_restaurant
from project.models import Customer, User, Owner, Restaurant, Ratings

class CustomerMethodTests(TestCase):
    def test_customer_ID_not_too_long(self):
        user = User(username="test_name", email="email@gmail.com")
        user.save()
        customer = Customer(customer_ID="1234567890123456789012345678901", user=user, email="123@gmail.com")
        customer.save()

        self.assertEqual((len(customer.customer_ID) <= 30 ), False)

    def test_customer_ID_correct_length(self):
        user = User(username="test_name", email="email@gmail.com")
        user.save()
        customer = Customer(customer_ID="12345678901234567890123456", user=user, email="123@gmail.com")
        customer.save()

        self.assertEqual(len(customer.customer_ID), 26)

    def test_email_not_too_long(self):
        user = User(username="test_name", email="email@gmail.com")
        user.save()
        customer = Customer(customer_ID="test", user=user, email="123456789012345678901234567890123456789012345678901")
        customer.save()

        self.assertEqual((len(customer.email) <= 50), False)

    def test_email_correct_length(self):
        user = User(username="test_name", email="email@gmail.com")
        user.save()
        customer = Customer(customer_ID="test", user=user, email="1234567890")
        customer.save()

        self.assertEqual(len(customer.email), 10)

class OwnerMethodTests(TestCase):
    def test_owner_ID_not_too_long(self):
        user = User(username="test_name", email="email@gmail.com")
        user.save()
        owner = Owner(owner_ID="1234567890123456789012345678901", user=user)
        owner.save()

        self.assertEqual((len(owner.owner_ID) <= 30), False)

    def test_owner_ID_correct_length(self):
        user = User(username="test_name", email="email@gmail.com")
        user.save()
        owner = Owner(owner_ID="12345678901234567890123456", user=user)
        owner.save()

        self.assertEqual(len(owner.owner_ID), 26)

class RestaurantMethodTests(TestCase):
    def test_default_address(self):
        restaurant = Restaurant(restaurant_ID="test_ID", name="testname", city="testcity", postcode="testpostcode",
                                category="testCategory", takeaway_option="yes")
        restaurant.save()

        self.assertEqual(restaurant.address, "")

    def test_correct_address(self):
        restaurant = Restaurant(restaurant_ID="test_ID", name="testname", city="testcity", postcode="testpostcode",
                                address="testaddress", category="testCategory", takeaway_option="yes")
        restaurant.save()

        self.assertEqual(restaurant.address, "testaddress")

    def test_default_city(self):
        restaurant = Restaurant(restaurant_ID="test_ID", name="testname", postcode="testpostcode",
                                address="testaddress", category="testCategory", takeaway_option="yes")
        restaurant.save()

        self.assertEqual(restaurant.city, "")

    def test_correct_city(self):
        restaurant = Restaurant(restaurant_ID="test_ID", name="testname", city="testcity", postcode="testpostcode",
                                address="testaddress", category="testCategory", takeaway_option="yes")
        restaurant.save()

        self.assertEqual(restaurant.city, "testcity")

    def test_correct_takeAway(self):
        restaurant = Restaurant(restaurant_ID="test_ID", name="testname", city="testcity", postcode="testpostcode",
                                address="testaddress", category="testCategory")
        restaurant.save()

        self.assertEqual(restaurant.takeaway_option, "yes")

    def test_correct_takeAway(self):
        restaurant = Restaurant(restaurant_ID="test_ID", name="testname", city="testcity", postcode="testpostcode",
                                address="testaddress", category="testCategory", takeaway_option="no")
        restaurant.save()

        self.assertEqual(restaurant.takeaway_option, "no")

class RatingsMethodTests(TestCase):
    def test_default_food_rating(self):
        user = User(username="test_name", email="email@gmail.com")
        user.save()
        customer = Customer(customer_ID="1", user=user, email="123@gmail.com")
        customer.save()
        restaurant = Restaurant(restaurant_ID="1", name="testname", city="testcity", postcode="testpostcode",
                                address="testaddress", category="testCategory", takeaway_option="yes")
        restaurant.save()
        rating = Ratings(service_Rating=5, atmosphere_Rating=5, price_Rating=5, comment="test")
        rating.save()

        self.assertEqual(rating.food_Rating, 0)

    def test_correct_food_rating(self):
        user = User(username="test_name", email="email@gmail.com")
        user.save()
        customer = Customer(customer_ID="1", user=user, email="123@gmail.com")
        customer.save()
        restaurant = Restaurant(restaurant_ID="1", name="testname", city="testcity", postcode="testpostcode",
                                address="testaddress", category="testCategory", takeaway_option="yes")
        restaurant.save()
        rating = Ratings(food_Rating=5, service_Rating=5, atmosphere_Rating=5, price_Rating=5, comment="test")
        rating.save()

        self.assertEqual(rating.food_Rating, 5)

    def test_default_service_rating(self):
        user = User(username="test_name", email="email@gmail.com")
        user.save()
        customer = Customer(customer_ID="1", user=user, email="123@gmail.com")
        customer.save()
        restaurant = Restaurant(restaurant_ID="1", name="testname", city="testcity", postcode="testpostcode",
                                address="testaddress", category="testCategory", takeaway_option="yes")
        restaurant.save()
        rating = Ratings(food_Rating=5, atmosphere_Rating=5, price_Rating=5, comment="test")
        rating.save()

        self.assertEqual(rating.service_Rating, 0)

    def test_correct_service_rating(self):
        user = User(username="test_name", email="email@gmail.com")
        user.save()
        customer = Customer(customer_ID="1", user=user, email="123@gmail.com")
        customer.save()
        restaurant = Restaurant(restaurant_ID="1", name="testname", city="testcity", postcode="testpostcode",
                                address="testaddress", category="testCategory", takeaway_option="yes")
        restaurant.save()
        rating = Ratings(food_Rating=5, service_Rating=5, atmosphere_Rating=5, price_Rating=5, comment="test")
        rating.save()

        self.assertEqual(rating.service_Rating, 5)

    def test_default_atmosphere_rating(self):
        user = User(username="test_name", email="email@gmail.com")
        user.save()
        customer = Customer(customer_ID="1", user=user, email="123@gmail.com")
        customer.save()
        restaurant = Restaurant(restaurant_ID="1", name="testname", city="testcity", postcode="testpostcode",
                                address="testaddress", category="testCategory", takeaway_option="yes")
        restaurant.save()
        rating = Ratings(food_Rating=5, service_Rating=5, price_Rating=5, comment="test")
        rating.save()

        self.assertEqual(rating.atmosphere_Rating, 0)

    def test_correct_atmosphere_rating(self):
        user = User(username="test_name", email="email@gmail.com")
        user.save()
        customer = Customer(customer_ID="1", user=user, email="123@gmail.com")
        customer.save()
        restaurant = Restaurant(restaurant_ID="1", name="testname", city="testcity", postcode="testpostcode",
                                address="testaddress", category="testCategory", takeaway_option="yes")
        restaurant.save()
        rating = Ratings(food_Rating=5, service_Rating=5, atmosphere_Rating=5, price_Rating=5, comment="test")
        rating.save()

        self.assertEqual(rating.atmosphere_Rating, 5)

    def test_default_price_rating(self):
        user = User(username="test_name", email="email@gmail.com")
        user.save()
        customer = Customer(customer_ID="1", user=user, email="123@gmail.com")
        customer.save()
        restaurant = Restaurant(restaurant_ID="1", name="testname", city="testcity", postcode="testpostcode",
                                address="testaddress", category="testCategory", takeaway_option="yes")
        restaurant.save()
        rating = Ratings(food_Rating=5, service_Rating=5, atmosphere_Rating=5, comment="test")
        rating.save()

        self.assertEqual(rating.price_Rating, 0)

    def test_correct_price_rating(self):
        user = User(username="test_name", email="email@gmail.com")
        user.save()
        customer = Customer(customer_ID="1", user=user, email="123@gmail.com")
        customer.save()
        restaurant = Restaurant(restaurant_ID="1", name="testname", city="testcity", postcode="testpostcode",
                                address="testaddress", category="testCategory", takeaway_option="yes")
        restaurant.save()
        rating = Ratings(food_Rating=5, service_Rating=5, atmosphere_Rating=5, price_Rating=5, comment="test")
        rating.save()

        self.assertEqual(rating.price_Rating, 5)

class HomeViewTests(TestCase):
    def test_home_view_with_no_restaurants(self):
        response = self.client.get(reverse('Rateaurant:home'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'There are no restaurants')
        self.assertQuerysetEqual(response.context['top_venues'], [])

    def test_home_view_with_restaurants(self):

        add_restaurant(RestaurantID="1", name="name1", category="asian", address="testaddress", city="testcity", postcode="testpostcode", image="none")

        response = self.client.get(reverse('Rateaurant:home'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "1")

class CategoriesViewTests(TestCase):
    def test_categories_view_with_categories(self):
        response = self.client.get(reverse('Rateaurant:categories'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Greek")
        self.assertContains(response, "Indian")
        self.assertContains(response, "Asian")

        num_categories = len(response.context['categories'])
        self.assertEquals(num_categories, 5)

class LoginViewTests(TestCase):
    def test_login_view_shows(self):
        response = self.client.get(reverse('Rateaurant:'))

        self.assertEqual(response.status_code, 200)

class RegisterViewTests(TestCase):
    def test_register_view_shows(self):
        response = self.client.get(reverse('Rateaurant:register'))

        self.assertEqual(response.status_code, 200)

class AddARestaurantViewTests(TestCase):
    def test_add_a_restaurant_view_shows(self):
        self.client = Client()
        self.user = User.objects.create_user('Jim', 'Jim@gmail.com', 'password')

        self.client.login(username='Jim', password='password')

        response = self.client.get(reverse('Rateaurant:addarestaurant'))

        self.assertEqual(response.status_code, 200)

class LogoutViewTests(TestCase):
    def test_logout_redirect(self):
        response = self.client.get(reverse('Rateaurant:logout'))

        self.assertRedirects(response, reverse('Rateaurant:home'), status_code=302, target_status_code=200, msg_prefix='',
                             fetch_redirect_response=True)