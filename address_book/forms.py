from django import forms 
from .models import Address

class AddressForm(forms.ModelForm):
    class Meta: 
        model = Address # this indicate the table to which the data will be saved
        fields = ["name", "email", "phone", "address", "city", "state", "zipcode"]