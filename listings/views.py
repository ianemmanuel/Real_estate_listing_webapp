
from django.shortcuts import render, redirect
from .models import Category, Listing
from django.views.generic import ListView, DetailView
# Create your views here.


def home(request):
	categories=Category.objects.all()
	data=Listing.objects.all()[:3]
	return render(request,'index/home.html',{'data':data, 'categories':categories})

# Category
def category_list(request):
    data=Category.objects.all().order_by('-id')
    return render(request,'index/categories.html',{'data':data})

# Comic-list according to category
def category_listings(request,cat_id):
	category=Category.objects.get(id=cat_id)
	data=Listing.objects.filter(category=category).order_by('-id')
	return render(request,'index/category_property_list.html',{
			'data':data,
			'category':category,
			})



# listings
class ListingsView(ListView):
	model = Listing
	ordering = ['-id']
	template_name = 'index/listings.html'

def listing_detail(request,slug,id):
	listing=Listing.objects.get(id=id)
	related_listings=Listing.objects.filter(category=listing.category).exclude(id=id)[:3]
	
	return render(request,'index/listing_detail.html',{'data':listing, 'related_listings': related_listings,
    'payment_type': dict(Listing.PAYMENT_TYPE)[listing.type]})



		
def tenancy(request):
     # Get all the available choices for the type field
    types = dict(Listing.PAYMENT_TYPE).values()
    
    # Pass the choices to the template
    context = {'types': types}
    return render(request,'index/tenancy.html',context)

def tenancy_listings_view(request,  type_name):
    listings = Listing.objects.filter(type__in=[k for k, v in Listing.PAYMENT_TYPE if v == type_name])
    context = {
        'listings': listings,
        'type_name': type_name
    }
    return render(request, 'index/tenancy_property_list.html', context)