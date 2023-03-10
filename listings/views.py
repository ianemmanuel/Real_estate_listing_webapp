
from django.shortcuts import render
from .models import Category, Listing, Banner
from django.views.generic import ListView, DetailView
# Create your views here.


# def index(request):
#     return render(request, 'index/home.html')

# Create your views here.
# Home Page
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
	
	return render(request,'index/listing_detail.html',{'data':listing,'related':related_listings})


# def listings(request):
# 	total_data=Listing.objects.count()
# 	data=Listing.objects.all().order_by('-id')
	
# 	return render(request,'index/listings.html',
# 	{
# 		'data':data,
# 		'total_data':total_data,
	
# 	})
		

# Product List According to Brand
# def publisher_comic_list(request,publisher_id):
# 	publisher=Location.objects.get(id=publisher_id)
# 	data=Listing.objects.filter(publisher=publisher).order_by('-id')
# 	return render(request,'publisher_comic_list.html',{
# 			'data':data,
# 			})


