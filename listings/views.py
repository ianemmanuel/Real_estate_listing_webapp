
from django.shortcuts import render
from .models import Category, Listing
from django.views.generic import ListView, DetailView
# Create your views here.


def index(request):
    return render(request, 'index/home.html')

# Create your views here.
# Home Page
def home(request):
	banners=Banner.objects.all().order_by('-id')
	data=Listing.objects.filter(is_featured=True).order_by('-id')
	return render(request,'landing_page.html',{'data':data,'banners':banners})

# Category
def category_list(request):
    data=Category.objects.all().order_by('-id')
    return render(request,'index/categories.html',{'data':data})



# listings
class ListingsView(ListView):
	model = Listing
	template_name = 'index/listings.html'

def listing_detail(request,slug,id):
	listing=Listing.objects.get(id=id)
	related_listings=Listing.objects.filter(category=listing.category).exclude(id=id)[:4]
	
	return render(request,'index/listing_detail.html',{'data':listing,'related':related_listings})


# def listings(request):
# 	total_data=Listing.objects.count()
# 	data=Listing.objects.all().order_by('-id')
	
# 	return render(request,'index/listings.html',
# 	{
# 		'data':data,
# 		'total_data':total_data,
	
# 	})
		
# Comic-list according to category
def category_listings(request,cat_id):
	category=Category.objects.get(id=cat_id)
	data=Listing.objects.filter(category=category).order_by('-id')
	return render(request,'category_product_list.html',{
			'data':data,
			})

# Product List According to Brand
# def publisher_comic_list(request,publisher_id):
# 	publisher=Location.objects.get(id=publisher_id)
# 	data=Listing.objects.filter(publisher=publisher).order_by('-id')
# 	return render(request,'publisher_comic_list.html',{
# 			'data':data,
# 			})
