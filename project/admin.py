from django.contrib import admin
from project.models import Customer, Owner, Restaurant, Ownership, Ratings
admin.site.register(Customer)
admin.site.register(Owner)
admin.site.register(Restaurant)
admin.site.register(Ownership)
admin.site.register(Ratings)
# Register your models here.
