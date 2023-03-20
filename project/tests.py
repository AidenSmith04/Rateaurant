from django.test import TestCase
from django.urls import reverse

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


def add_restaurant(self, restaurant_id, name, city, postcode, address, category, takeaway_option):
    restaurant = Restaurant(restaurant_ID=restaurant_id, name=name, city=city, postcode=postcode,
                                        address=address, category=category, takeaway_option=takeaway_option)
    restaurant.save()
    return restaurant

class HomeViewTests(TestCase):


    def test_home_view_with_restaurants(self):
        add_restaurant(self, "1", "name1", "city1", "postcode1", "address1", "category1", "yes")
        add_restaurant(self, "1", "name2", "city2", "postcode2", "address2", "category2", "yes")
        add_restaurant(self, "1", "name3", "city3", "postcode3", "address3", "category3", "yes")
        add_restaurant(self, "1", "name1", "city4", "postcode4", "address4", "category4", "yes")
        add_restaurant(self, "1", "name5", "city5", "postcode5", "address5", "category5", "yes")
        add_restaurant(self, "1", "name6", "city6", "postcode6", "address6", "category6", "yes")
        add_restaurant(self, "1", "name7", "city7", "postcode7", "address7", "category7", "yes")
        add_restaurant(self, "1", "name8", "city8", "postcode8", "address8", "category8", "yes")
        add_restaurant(self, "1", "name9", "city9", "postcode9", "address9", "category9", "yes")
        add_restaurant(self, "1", "name10", "city10", "postcode10", "address10", "category10", "yes")

        response = self.client.get(reverse('Rateaurant:home'))

        self.assertContains(response, "name1")
        self.assertQuerysetEqual(response.context['top_venues'], 0)