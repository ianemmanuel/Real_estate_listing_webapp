
from django.shortcuts import render, redirect
from .models import Category, Listing
from django.views.generic import ListView, DetailView

#Recommendation
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer


# Create your views here.


def home(request):
	categories=Category.objects.all()
	data=Listing.objects.all().order_by('-id')[:3]
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


def recommendation(request):
	pid=request.GET['comic']
	listing=Listing.objects.get(pk=pid)
	# from google.colab import files
	# uploaded = files.upload()
	df = pd.read(listing)
	df.head(3)
	 # Get a count of the number of rows/ movies in the data set and the number of columns
	df.shape
		# Create a list of important columns for the recommendation engine
	columns = ['category', 'price','publisher','author','title']
		# Show the data
	df[columns].head(3)
		# Check for any missing values in the important columns
	df[columns].isnull().values.any()

	#	 Create a function to combine the values of the important columns into a single string
	def get_important_features(data):
		important_features = []
		for i in range(0, data.shape[0]):
			important_features.append(data['category'][i]+data['price'][i]+data['location'][i]+data['author'][i]+data['title'][i])
		return important_features

	df ['important_features'] = get_important_features(df)

	df.head(3)

	cm = CountVectorizer().fit_transform(df['important_features'])

# Get the cosine similarity matrix from the count matrix
	cs= cosine_similarity(cm)
	print(cs)
	
	cs.shape
	predictor_event = listing

	movie_id = df[df.title==predictor_event]['Event_id'].values[0]
	scores = list(enumerate(cs[movie_id]))
	sorted_scores = sorted(scores, key = lambda x:x[1], reverse = True)
	sorted_scores = sorted_scores[1:]
	print(sorted_scores)
	j = 0
	print('The 7 most recommended movies are: ')
	for item in sorted_scores:
		comic_title = df[df.Movie_id == item[0]]['title'].values[0]
		print(j+1, comic_title)
		j = j+1
		if j>4:
			break
	return render(request, 'listing_detail.html',{'comic_title':comic_title})
