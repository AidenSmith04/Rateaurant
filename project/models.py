from django.db import models
from django.contrib.auth.models import User


# Create your models here
class Customer(models.Model):
    customer_ID = models.CharField(max_length=30, primary_key=True, unique=True, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.customer_ID
    
class Owner(models.Model):
    owner_ID = models.CharField(max_length=30, primary_key=True, unique=True,on_delete = models.CASCADE) 
    owner = models.OneToOneField(User, on_delete=models.CASCADE) 
    def __str__(self):
        return self.owner_ID
    
class Restaurant(models.Model):
    restraunt_ID = models.CharField(max_length=30, primary_key=True, unique=True, on_delete= models.CASCADE)
    name = models.CharField(max_length=50)
    postcode = models.CharField(max_length=50)
    category = models.CharField(max_length=30)
    takeaway_option = models.BooleanField(default=True)
    
    def __str__(self):
        return self.restraunt_ID

class Ownership():
    owner_ID = models.ForeignKey(Owner)
    restraunt_ID = models.ForeignKey(Restaurant)
    def __str__(self):
        return "%s %s " % (self.owner_ID, self.restraunt_ID)
    
class Ratings(models.Model):
   
    class Rating_Values(models.IntegerChoices):
        NO_STAR = 0
        ONE_STAR = 1
        TWO_STARS = 2
        THREE_STARS = 3
        FOUR_STARS = 4
        FIVE_STARS = 5
   
    customer_ID = models.ManyToManyField(Customer)
    restraunt_ID = models.ManyToManyField(Restaurant)
    food_Rating = models.IntegerField(choices=Rating_Values.choices)
    service_Rating = models.IntegerField(choices=Rating_Values.choices)
    atmosphere_Rating = models.IntegerField(choices=Rating_Values.choices)
    price_Rating = models.IntegerField(choices=Rating_Values.choices)
    favourited = models.BooleanField(default=False)
    comment = models.CharField(max_length=300)
    def __str__(self):
        return self.comment