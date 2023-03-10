from django.db import models
from django.contrib.auth.models import User


# Create your models here
class Customer(models.Model):
    customer_ID = models.CharField(max_length=30, primary_key=True, unique=True)
    user = models.OneToOneField(User, primary_key=False, on_delete=models.CASCADE)

    email = models.CharField(max_length=50)


    def __str__(self):
        return self.customer_ID


class Owner(models.Model):
    owner_ID = models.CharField(max_length=30,primary_key=True, unique=True)
    user = models.OneToOneField(User,primary_key= False, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.owner_ID


class Restaurant(models.Model):
    restaurant_ID = models.CharField(max_length=30, primary_key=True, unique=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50, default="")
    city = models.CharField(max_length=30, default="")
    postcode = models.CharField(max_length=50)
    category = models.CharField(max_length=30)
    takeaway_option = models.CharField(max_length= 3, default="yes")

    def __str__(self):
        return self.restaurant_ID


class Ownership(models.Model):
    restaurant_ID = models.OneToOneField(Restaurant, on_delete=models.CASCADE, primary_key=True)
    owner_ID = models.ForeignKey(Owner, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s " % (self.restaurant_ID, self.owner_ID)
    
class Favourited(models.Model):
    cust_id = models.ForeignKey(Customer, on_delete=models.CASCADE, default =1)
    rest_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return "%s %s" % (self.cust_id, self.rest_id)



class Ratings(models.Model):
    NO_STAR = 0
    ONE_STAR = 1
    TWO_STARS = 2
    THREE_STARS = 3
    FOUR_STARS = 4
    FIVE_STARS = 5
    RATING_CHOICES = [(NO_STAR, "0"), (ONE_STAR, "1"), (TWO_STARS, "2"), (THREE_STARS, "3"), (FOUR_STARS, "4"),
                      (FIVE_STARS, "5"), ]

    cust_id = models.ForeignKey(Customer, on_delete=models.CASCADE, default=1)
    rest_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE, default=1)
    food_Rating = models.IntegerField(choices=RATING_CHOICES, default=NO_STAR)
    service_Rating = models.IntegerField(choices=RATING_CHOICES, default=NO_STAR)
    atmosphere_Rating = models.IntegerField(choices=RATING_CHOICES, default=NO_STAR)
    price_Rating = models.IntegerField(choices=RATING_CHOICES, default=NO_STAR)
    comment = models.CharField(max_length=300)

    def __str__(self):
        return self.comment
