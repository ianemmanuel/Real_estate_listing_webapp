from django import forms
from .models import Listing


 



class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields =('title','number_of_bedrooms','number_of_bathrooms','address','area_sqft','detail','video','type','price','category')

        widgets = {
            'title':forms.TextInput(attrs={'class':'inputBox'}),
            'number_of_bedrooms':forms.NumberInput(attrs={'class':'inputBox'}),
            'number_of_bathrooms':forms.NumberInput(attrs={'class':'inputBox'}),
            'address':forms.TextInput(attrs={'class':'inputBox'}),
            'area_sqft':forms.NumberInput(attrs={'class':'inputBox'}),
            'detail':forms.Textarea(attrs={'class':'inputBox'}),
            'video':forms.TextInput(attrs={'class':'inputBox'}),
            'type':forms.Select(attrs={'class':'inputBox'}),
            'price':forms.NumberInput(attrs={'class':'inputBox'}),
            'category':forms.Select(attrs={'class':'inputBox'}),
            
        }