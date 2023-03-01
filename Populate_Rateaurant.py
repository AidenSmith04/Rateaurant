import requests 
import xmltodict
import random
import string



def generateID():
    characters = string.ascii_letters + string.digits
    ret = ''.join(random.choice(characters) for i in range(30))
    return ret 

def generatePassword():
    characters: string.ascii_letters + string.digits + string.punctuation
    ret = ''.join(random.choice(characters) for i in range(10))
    return ret

 
def populate_restruant():
    url = "https://ratings.food.gov.uk/OpenDataFiles/FHRS776en-GB.xml"
    response = requests.get(url)
    data = xmltodict.parse(response.content)
    ret = data["FHRSEstablishment"]["EstablishmentCollection"]["EstablishmentDetail"]
    dict = {}
    wanted = ["Zizzi","Wagamama", "Ubiquitous chip", "The Ivy",  "The Finnieston", "Ramen Dayo", "Paesano Pizza", "Ox and Finch", "Mozza", "Mother India", "Little Italy", "Joia Italian Restraunt and Bar", "Gyros", "Fat Hippo Glasgow", "Chimes of India", "BRGR", "Bella Italia", "American NY Grill", "Lamora Pizzeria", "Oran Mor", "Chaiiwala", "Chaophraya", "The Butchershop Bar and Grill", "Cranachan"]

    italian = ["Zizzi", "Paesano Pizza", "Mozza", "Little Italy", "Joia Italian Restraunt and Bar", "Bella Italia", "Lamora Pizzeria"]
    asian = ["Wagamama", "Ramon Dayo"]
    indian = ["Mother India", "Chimes of India","Chaiiwala", "Chaophraya"]
    greek = ["Gyros"]
    grill = ["Fat Hippo Glasgow", "BRGR", "American NY Grill","The Butchershop Bar and Grill"]
    contemprary = ["Ubiquitous chip", "The Ivy", "The Finnieston", "Ox and Finch", "Oran Mor", "Cranachan"]
   
    for i in range(len(ret)):
     temp_list = ret[i].keys()
     if ret[i]["BusinessName"] in wanted and "PostCode" in temp_list and ret[i]["BusinessType"] != "Takeaway/sandwich shop":
    
              
                dict[generateID()] = {"Name": ret[i]["BusinessName"], "Category": ret[i]["BusinessType"], "PostCode": ret[i]["PostCode"]}
                
                wanted.remove(ret[i]["BusinessName"])

    for key in dict.keys():
        if(dict[key]["Name"] in italian):
            dict[key]["Category"] = "Italian"
        elif(dict[key]["Name"] in asian):
            dict[key]["Category"] = "Asian"
        elif(dict[key]["Name"] in indian):
            dict[key]["Category"] = "Indian"
        elif(dict[key]["Name"] in greek):
          dict[key]["Category"] = "Greek"
        elif(dict[key]["Name"] in grill):
            dict[key]["Category"] = "Grill"
        elif(dict[key]["Name"] in contemprary):
            dict[key]["Category"] = "contemporary"
        print(dict[key])
        print("\n")
    return dict
    


def populate_customer():
    customerusername = ["joshM", "LukeJ", "JohnDoe", "BobJoe", "Foody101", "keyGreen", "CraneC", "sunsetty", "Joey", "Burpy"]
    customerEmail = ["joshM@mail.com", "LukeJ@mail.com", "JohnDoe@mail.com", "BobJoe@mail.com", "Foody101@mail.com", "keyGreen@mail", "CraneC@mail", "sunsetty@mail.com", "joey@mail.com","Burpy@mail.com"]
    dict = {}
    for i in range(len(customerusername)):
        dict[generateID()] = {"Username":customerusername[i], "Password":generatePassword(), "Email":customerEmail[i]}
    return dict

def populate_owner():
    ownerusername = ["Martyj", "joema", "greeny", "termy", "marval", "owner1000", "Historicfood", "Rougetaste", "blender12", "Boydie", "rango", "django23", "MasterChef", "chefy", "chiefton", "cheffy","nutriousion", "googler", "owner1", "owner2" ]    
    owneremail = ["Martyj@mail.com", "joema@mail.com", "greeny@mail.com", "termy@mail.com", "marval@mail.com", "owner1000@mail.com", "Historicfood@mil.com", "Rougetaste@mail.com", "blender12@mail.com", "Boydie@mail.com", "rango@mail.com", "django23@mail.com", "MasterChef@mail.com", "chefy@mail.com", "chiefton@mail.com", "cheffy@mail.com","nutriousion@mail.com", "googler@mail.com", "owner1@mail.com", "owner2@mail.com"]
    dict = {}
    for i in range(len(ownerusername)):
        dict[generateID()] = {"Username": ownerusername[i], "Password":generatePassword(), "Email":owneremail[i]}
    return dict
        
def populate_ownership(restruants, owners):
    dict={}
    list_owner = owners.keys()
    list_restraunt = restruants.keys()
    for i in range(len(list_owner)):
        dict[list_restraunt[i]] = list_owner[i]
    return dict 


    
def populate_ratings(restraunts, customer):
    dict= {}
    rate = {"Excellent":[("food_rating",5) , ("service_rating", 5), ("atmosphere_rating", 5), ("price_rating",5), ("favourited", True), ("comment","The best restraunt I have ever been to would recommend")],
             "Good":[("food_rating",4), ("service_rating", 4), ("atmosphere_rating", 4), ("price_rating",4), ("favourited", True), ("comment","Good restraunt for a night out")],
            "Average":[("food_rating",3), ("service_rating", 3), ("atmosphere_rating", 3), ("price_rating",3), ("favourited",False) , ("comment","Not a bad restraunt but nothing special about it")],
            "Poor":[("food_rating",2), ("service_rating", 2), ("atmosphere_rating", 2), ("price_rating",2), ("favourited", False), ("comment","Not a good experience I do not recommend")],
            "Bad":[("food_rating",1), ("service_rating", 1), ("atmosphere_rating",1), ("price_rating",1), ("favourited", False), ("comment","Waited 3 hours before the food came and it was over priced slop")],
            "Terrible":[("food_rating",0), ("service_rating", 0), ("atmosphere_rating", 0), ("price_rating",0), ("favourited", False), ("comment","Got the worst food poisoning of my life")],
            "Complex1":[("food_rating",5), ("service_rating", 2), ("atmosphere_rating", 5), ("price_rating",5), ("favourited", True), ("comment","Wonderful restraunt exept the service is terrible")],
            "Complex2":[("food_rating",3), ("service_rating", 5), ("atmosphere_rating", 5), ("price_rating",5), ("favourited", False), ("comment","Wonderful place and people but unfortunalty the food was terrible")],
            "Complex3":[("food_rating",5), ("service_rating", 5), ("atmosphere_rating", 1), ("price_rating",1), ("favourited", False), ("comment","Amazing food and waiters but over  priced and full of snobbish customers")],
            "Complex4":[("food_rating",2), ("service_rating", 2), ("atmosphere_rating", 5), ("price_rating",5), ("favourited", False), ("comment","would clarify as a restraunt for students thats the food quality and vibe")]}
    list_restraunts = restraunts.keys()
    list_customer = customer.keys()
    rate_keys = rate.keys()
    count = 0
    reverse = False
    
    
    for i in range(len(list_restraunts)):
        if count != len(list_customer)-1 and reverse == False:
            temp = rate[rate_keys[count]]
            temp.insert(0, ("RestrauntID",list_restraunts[i]))
            temp.insert(0,("CustomerID", list_customer[count]))
            dict[i] = {key: value for (key, value) in temp}
            count+=1
        elif count == len(list_customer)-1 or reverse ==True:
            reverse == True
            temp = rate[rate_keys[count]]
            temp.insert(0, ("RestrauntID",list_restraunts[i]))
            temp.insert(0,("CustomerID", list_customer[count]))
            dict[i] = {key: value for (key, value) in temp}
            count-=1
    return dict
                
        
    





##{Ratingnum: {CustomerID:val, restrauntID:val, food_rating:val, service_rating:val, atmosphere_rating:val, price_rating:val, favourited:val, comment:val}}