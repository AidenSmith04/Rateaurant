import requests
import xmltodict
import random
import string
import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Rateaurant.settings')

import django

django.setup()
from project.models import Customer, Owner, Restaurant, Ownership, Ratings, Favourited
from django.contrib.auth.models import User


def getImagePath():
    path = os.getcwd() + "/media/Restaurant_pics"
    return path

def generateID():
    characters = string.ascii_letters + string.digits
    ret = ''.join(random.choice(characters) for i in range(30))
    return ret


def generatePassword():
    characters = string.ascii_letters + string.digits + string.punctuation
    ret = ''.join(random.choice(characters) for i in range(10))
    return ret


def populate_restaurant():
    path = getImagePath()
    url = "https://ratings.food.gov.uk/OpenDataFiles/FHRS776en-GB.xml"
    response = requests.get(url)
    data = xmltodict.parse(response.content)
    ret = data["FHRSEstablishment"]["EstablishmentCollection"]["EstablishmentDetail"]
    dict = {}
    wanted = ["Zizzi", "Wagamama", "Ubiquitous chip", "The Ivy", "The Finnieston", "Ramen Dayo", "Paesano Pizza",
              "Ox and Finch", "Mozza", "Mother India", "Little Italy", "Joia Italian Restraunt and Bar", "Gyros",
              "Fat Hippo Glasgow", "Chimes of India", "BRGR", "Bella Italia", "American NY Grill", "Lamora Pizzeria",
              "Oran Mor", "Chaiiwala", "Chaophraya", "The Butchershop Bar and Grill", "Cranachan"]
    
    pic_dict = {"Zizzi":path +"/zizzi.jpg", "Wagamama":path+"/wagamama.jpg", "Ubiquitous chip":path+"/chip.jpg", "The Ivy":path+"/ivy.jpg", "The Finnieston":path+"/finnie.jpg", "Ramen Dayo":path+"/Ramen.jpg", "Paesano Pizza":path+"/paesano.jpg",
              "Ox and Finch":path+"/ox.jpg", "Mozza":path+"/mozza.jpg", "Mother India":path+"/mother.jpg", "Little Italy":path+"/little_italy.jpg", "Joia Italian Restraunt and Bar":path+"/joia.jpg", "Gyros":path+"/gyro.jpg",
              "Fat Hippo Glasgow":path+"/fat.jpg", "Chimes of India":path+"/chimes.jpg", "BRGR":path+"/brgr.jpg", "Bella Italia":path+"/bella.jpg", "American NY Grill":path+"/NY.jpg", "Lamora Pizzeria":path+"/lamora.jpg",
              "Oran Mor":path+"/oran.jpg", "Chaiiwala":path+"/chaiiwala.jpg", "Chaophraya":path+"/Chaophreya", "The Butchershop Bar and Grill":path+"/butcher.jpg", "Cranachan":path+"/cran.jpg"}

    italian = ["Zizzi", "Paesano Pizza", "Mozza", "Little Italy", "Joia Italian Restraunt and Bar", "Bella Italia",
               "Lamora Pizzeria"]
    asian = ["Wagamama", "Ramon Dayo"]
    indian = ["Mother India", "Chimes of India", "Chaiiwala", "Chaophraya"]
    greek = ["Gyros"]
    grill = ["Fat Hippo Glasgow", "BRGR", "American NY Grill", "The Butchershop Bar and Grill"]
    contemporary = ["Ubiquitous chip", "The Ivy", "The Finnieston", "Ox and Finch", "Oran Mor", "Cranachan"]

    for i in range(len(ret)):
        temp_list = ret[i].keys()
        if ret[i]["BusinessName"] in wanted and "PostCode" in temp_list and ret[i][
            "BusinessType"] != "Takeaway/sandwich shop":
            dict[str(i*45)] = {"Name": ret[i]["BusinessName"], "Category": ret[i]["BusinessType"],
                                  "Address": ret[i]["AddressLine2"], "City": ret[i]["AddressLine3"],
                                  "PostCode": ret[i]["PostCode"], "Image":pic_dict[ret[i]["BusinessName"]]}
            wanted.remove(ret[i]["BusinessName"])

    for key in dict.keys():
        if (dict[key]["Name"] in italian):
            dict[key]["Category"] = "Italian"
        elif (dict[key]["Name"] in asian):
            dict[key]["Category"] = "Asian"
        elif (dict[key]["Name"] in indian):
            dict[key]["Category"] = "Indian"
        elif (dict[key]["Name"] in greek):
            dict[key]["Category"] = "Greek"
        elif (dict[key]["Name"] in grill):
            dict[key]["Category"] = "Grill"
        elif (dict[key]["Name"] in contemporary):
            dict[key]["Category"] = "Contemporary"
    return dict


def populate_customer():
    customerusername = ["joshM", "LukeJ", "JohnDoe", "BobJoe", "Foody101", "keyGreen", "CraneC", "sunsetty", "Joey",
                        "Burpy"]
    customerEmail = ["joshM@mail.com", "LukeJ@mail.com", "JohnDoe@mail.com", "BobJoe@mail.com", "Foody101@mail.com",
                     "keyGreen@mail", "CraneC@mail", "sunsetty@mail.com", "joey@mail.com", "Burpy@mail.com"]
    dict = {}
    for i in range(len(customerusername)):
        dict[str(i)] = {"Username": customerusername[i], "Password": "PASSW0RD",
                              "Email": customerEmail[i]}
    return dict


def populate_owner():
    ownerusername = ["Martyj", "joema", "greeny", "termy", "marval", "owner1000", "Historicfood", "Rougetaste",
                     "blender12", "Boydie", "rango", "django23", "MasterChef", "chefy", "chiefton", "cheffy",
                     "nutriousion", "googler", "owner1", "owner2"]
    owneremail = ["Martyj@mail.com", "joema@mail.com", "greeny@mail.com", "termy@mail.com", "marval@mail.com",
                  "owner1000@mail.com", "Historicfood@mil.com", "Rougetaste@mail.com", "blender12@mail.com",
                  "Boydie@mail.com", "rango@mail.com", "django23@mail.com", "MasterChef@mail.com", "chefy@mail.com",
                  "chiefton@mail.com", "cheffy@mail.com", "nutriousion@mail.com", "googler@mail.com", "owner1@mail.com",
                  "owner2@mail.com"]
    dict = {}
    for i in range(len(ownerusername)):
        dict[str(i*33)] = {"Username": ownerusername[i], "Password": "PASSW0RD", "Email": owneremail[i]}
    return dict


def populate_ownership(restaurants, owners):
    dict = {}
    for i in range(len(restaurants)):
        dict[restaurants[i]] = owners[i]
    return dict


def populate_ratings(restaurants, customer):
    dict = {}
    rate = {0: [("food_rating", 5), ("service_rating", 5), ("atmosphere_rating", 5), ("price_rating", 5),
                          ("favourited", True), ("comment", "The best restraunt I have ever been to would recommend")],
            1: [("food_rating", 4), ("service_rating", 4), ("atmosphere_rating", 4), ("price_rating", 4),
                     ("favourited", True), ("comment", "Good restraunt for a night out")],
            2: [("food_rating", 3), ("service_rating", 3), ("atmosphere_rating", 3), ("price_rating", 3),
                        ("favourited", False), ("comment", "Not a bad restraunt but nothing special about it")],
            3: [("food_rating", 2), ("service_rating", 2), ("atmosphere_rating", 2), ("price_rating", 2),
                     ("favourited", False), ("comment", "Not a good experience I do not recommend")],
            4: [("food_rating", 1), ("service_rating", 1), ("atmosphere_rating", 1), ("price_rating", 1),
                    ("favourited", False),
                    ("comment", "Waited 3 hours before the food came and it was over priced slop")],
            5: [("food_rating", 0), ("service_rating", 0), ("atmosphere_rating", 0), ("price_rating", 0),
                         ("favourited", False), ("comment", "Got the worst food poisoning of my life")],
            6: [("food_rating", 5), ("service_rating", 2), ("atmosphere_rating", 5), ("price_rating", 5),
                         ("favourited", True), ("comment", "Wonderful restraunt exept the service is terrible")],
            7: [("food_rating", 3), ("service_rating", 5), ("atmosphere_rating", 5), ("price_rating", 5),
                         ("favourited", False),
                         ("comment", "Wonderful place and people but unfortunalty the food was terrible")],
            8: [("food_rating", 5), ("service_rating", 5), ("atmosphere_rating", 1), ("price_rating", 1),
                         ("favourited", False),
                         ("comment", "Amazing food and waiters but over  priced and full of snobbish customers")],
            9: [("food_rating", 2), ("service_rating", 2), ("atmosphere_rating", 5), ("price_rating", 5),
                         ("favourited", False),
                         ("comment", "would clarify as a restraunt for students thats the food quality and vibe")]}

    
    count =0
    for i in restaurants:
       
        if count <= 9:
            temp = rate[count].copy()
            temp.insert(0, ("RestaurantID",i))
            temp.insert(0, ("CustomerID", customer[count]))
            dict[count] = {key: value for (key, value) in temp}
            count+=1
        elif count > 9:
            temp = rate[count-10].copy()
            temp.insert(0, ("RestaurantID",i))
            temp.insert(0, ("CustomerID", customer[count-10]))
            dict[count] = {key: value for (key, value) in temp}
            count += 1
        
    return dict


def add_restaurant(RestaurantID, name, category, address, city, postcode, image, takeaway_option="yes"):
    r = Restaurant.objects.create(restaurant_ID=RestaurantID)
    r.name = name
    r.category = category
    r.address = address
    r.city = city
    r.postcode = postcode
    r.picture = image
    r.takeaway_option = takeaway_option
    r.save()
    return r


def add_customer(customerID, username, password, email):
    
    user = User(username = username, email = email)
    user.set_password(password)
    user.save()
    c = Customer.objects.create(customer_ID = customerID, user = user)
 
    c.save()
    return c


def add_owner(ownerID, username, password, email):
    owner = User(username = username, email = email)
    owner.set_password(password)
    owner.save()
    o = Owner.objects.create(owner_ID = ownerID, user = owner)
    o.save()
    return o


def add_ownership(restaurantID, ownerID):
    own = Ownership.objects.create(restaurant_ID=restaurantID, owner_ID=ownerID)
    own.save()
    return own


def add_ratings(customerID, restaurantID, foodRating, serviceRating, atmosphereRating, priceRating, comment):
    rate = Ratings.objects.create(cust_id=customerID, rest_id=restaurantID, food_Rating=foodRating,
                                         service_Rating=serviceRating, atmosphere_Rating=atmosphereRating,
                                         price_Rating=priceRating, comment=comment)
    rate.save()
    return rate

def add_favourite(customerID, restaurantID):
    fav = Favourited.objects.create(cust_id = customerID, rest_id = restaurantID)
    fav.save()
    return fav

##CREATE POPULATION FOR FAVOURITE TABLE

def populate():
    owner = populate_owner()
    customer = populate_customer()
    restaurant = populate_restaurant()
    listowne = []
    listrest = []
    listcust = []
   
    for customers, customer_data in customer.items():
        
        cust = add_customer(customers, customer_data["Username"], customer_data["Password"], customer_data["Email"])
        listcust.append(cust)

    for owners, owner_data in owner.items():
        own = add_owner(owners, owner_data["Username"], owner_data["Password"], owner_data["Email"])
        listowne.append(own)

    for restaurants, restaurant_data in restaurant.items():
        rest = add_restaurant(restaurants, restaurant_data["Name"], restaurant_data["Category"],
                              restaurant_data["Address"], restaurant_data["City"], restaurant_data["PostCode"], restaurant_data["Image"])
        listrest.append(rest)

    ownership = populate_ownership(listrest, listowne)
    rating = populate_ratings(listrest, listcust)

    for key, val in ownership.items():
        add_ownership(key, val)
 
    for key, val in rating.items():
        add_ratings(val["CustomerID"], val["RestaurantID"], val["food_rating"], val["service_rating"], val["atmosphere_rating"], val["price_rating"], val["comment"])
        if(val["favourited"]):
            add_favourite(val["CustomerID"], val["RestaurantID"])
 



if __name__ == '__main__':
    print('Starting Rateaurant population script...')
    populate()
    print("....Finished population script ")
