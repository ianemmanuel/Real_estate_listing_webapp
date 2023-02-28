from django import forms
from .models import Listing


 
class CustomDateInput(forms.DateInput):
    input_type = 'datetime-local'


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields =('title','price','category','Agent','type','number_of_bedrooms','number_of_bathrooms','address','area_sqft','detail','video', 'open_house_date')

        widgets = {
            'title':forms.TextInput(attrs={'class':'inputBox'}),
            'number_of_bedrooms':forms.NumberInput(attrs={'class':'inputBox'}),
            'number_of_bathrooms':forms.NumberInput(attrs={'class':'inputBox'}),
            'address':forms.TextInput(attrs={'class':'inputBox'}),
            'area_sqft':forms.NumberInput(attrs={'class':'inputBox'}),
            'detail':forms.Textarea(attrs={'class':'inputBox'}),
            'video':forms.FileInput(),
            'type':forms.Select(attrs={'class':'inputBox'}),
            'price':forms.NumberInput(attrs={'class':'inputBox'}),
            'category':forms.Select(attrs={'class':'inputBox'}),
            # 'Agent':forms.Select(attrs={'class':'inputBox'}),
            'Agent': forms.TextInput(attrs={'class':'inputBox','value': '', 'id': 'agent_id', 'type':'hidden'}),
            'open_house_date': CustomDateInput(format='%Y-%m-%d %H:%M:%S')
            
        }

class UpdateListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields =('title','price','category','type','number_of_bedrooms','number_of_bathrooms','address','area_sqft','detail','video', 'open_house_date')

        widgets = {
            'title':forms.TextInput(attrs={'class':'inputBox'}),
            'number_of_bedrooms':forms.NumberInput(attrs={'class':'inputBox'}),
            'number_of_bathrooms':forms.NumberInput(attrs={'class':'inputBox'}),
            'address':forms.TextInput(attrs={'class':'inputBox'}),
            'area_sqft':forms.NumberInput(attrs={'class':'inputBox'}),
            'detail':forms.Textarea(attrs={'class':'inputBox'}),
            'video':forms.FileInput(),
            'type':forms.Select(attrs={'class':'inputBox'}),
            'price':forms.NumberInput(attrs={'class':'inputBox'}),
            'category':forms.Select(attrs={'class':'inputBox'}),
            'open_house_date':CustomDateInput(format='%Y-%m-%d %H:%M:%S')
            
        }