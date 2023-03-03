from django.db import models



# Create your models here
class Customer(models.Model):
    customer_ID = models.CharField(max_length=30, primary_key=True, unique=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.EmailField()
   
    def __str__(self):
        return self.customer_ID

class Owner(models.Model):
    owner_ID = models.CharField(max_length=30, primary_key=True, unique=True) 
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.EmailField()
    def __str__(self):
        return self.owner_ID
    
class Restaurant(models.Model):
    restaurant_ID = models.CharField(max_length=30, primary_key=True, unique=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50, default="")
    city = models.CharField(max_length=30, default="")
    postcode = models.CharField(max_length=50)
    category = models.CharField(max_length=30)
    takeaway_option = models.BooleanField(default=True)

    def __str__(self):
        return self.restaurant_ID

class Ownership(models.Model):
    restaurant_ID = models.OneToOneField(Restaurant, on_delete=models.CASCADE, primary_key=True)
    owner_ID = models.ForeignKey(Owner, on_delete=models.CASCADE)
    def __str__(self):
        return "%s %s " % (self.restaurant_ID,self.owner_ID)
    
class Ratings(models.Model):

    class Rating_Values(models.IntegerChoices):
        NO_STAR = 0
        ONE_STAR = 1
        TWO_STARS = 2
        THREE_STARS = 3
        FOUR_STARS = 4
        FIVE_STARS = 5
   
    cust_id = models.ForeignKey(Customer, on_delete=models.CASCADE, default=1)
    rest_id = models.ForeignKey(Restaurant,on_delete=models.CASCADE, default=1)
    food_Rating = models.IntegerField(choices=Rating_Values.choices)
    service_Rating = models.IntegerField(choices=Rating_Values.choices)
    atmosphere_Rating = models.IntegerField(choices=Rating_Values.choices)
    price_Rating = models.IntegerField(choices=Rating_Values.choices)
    favourited = models.BooleanField(default=False)
    comment = models.CharField(max_length=300)
    def __str__(self):
        return self.comment