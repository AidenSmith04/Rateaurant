from django import forms
from project.models import Customer, Owner, Restaurant, Ownership, Ratings, Favourited
from django.contrib.auth.models import User

# Choices fields for dropdown menu form input

Categories = {
    ('Italian', 'Italian'),
    ('Asian', 'Asian'),
    ('Indian', 'Indian'),
    ('Greek', 'Greek'),
    ('Contemporary', 'Contemporary'),
}

YesNo = {
    ('Yes', 'Yes'),
    ('No', 'No')
}


class RestaurantForm(forms.ModelForm):
    name = forms.CharField(max_length=50, help_text="Please enter the name of the venue.")
    address = forms.CharField(max_length=50, help_text="Please enter the address of the page.")
    city = forms.CharField(max_length=30, help_text="Please enter the city of the venue.")
    postcode = forms.CharField(max_length=50, help_text="Please enter the postcode of the venue.")
    category = forms.CharField(widget=forms.Select(choices=Categories),
                               help_text="Please enter the category of the venue.")
    takeaway_option = forms.CharField(widget=forms.Select(choices=YesNo), help_text="")

    class Meta:
        model = Restaurant
        fields = ('name', 'address', 'city', 'postcode', 'category', 'picture', 'takeaway_option')


class UserForm(forms.ModelForm):
    password = forms.CharField(max_length=30, widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password',)
        help_texts = {
            'username': None
        }


class CustomerForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Customer
        fields = ('email',)


class OwnerForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Owner
        fields = ('email',)


class OwnershipForm(forms.ModelForm):
    class Meta:
        model = Ownership
        exclude = ('owner_ID', 'restaurant_ID')


class ReviewForm(forms.ModelForm):
    comment = forms.CharField(max_length=300, required=False)
    forms
    class Meta:
        model = Ratings
        fields = ('comment',)


class FavouriteForm(forms.ModelForm):
    field = forms.BooleanField(widget=forms.Select(attrs={'onchange': 'submit();'}))

    class Meta:
        model = Favourited
        fields = ('field',)
