# Rateaurant

Make sure to imput the following commands in the command prompt:

pip install requests

pip install xmltodict

If you get a table doesnt exist error:
1) Go into project/migrations and delete everything except for the __pycache__ file.
	NOTE: delete the files inside the __pycache__ folder but not the folder itself
2) Delete db.sqlite3 in the top folder
3) python manage.py makemigrations project
4) python manage.py migrate

Aiden:
- Add Bootstrap

Joshua:
- Fix database for favourites

Sami:
- Chilling.py

Luke:
- Add a rating
- Add favourite
- Create a logo
- Add validation for rating

Khalis:
- Implement Google maps API
