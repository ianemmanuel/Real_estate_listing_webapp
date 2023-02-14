
from django.urls import path
from .import  views

urlpatterns=[
     path('',views.index, name='index'),
     path('category-list',views.category_list,name='categories'),
     path('listings',views.ListingsView.as_view(),name='listings'),
     path('categories/<int:cat_id>',views.category_listings,name='categories'),
     path('listing/<str:slug>/<int:id>', views.listing_detail, name='listing')

]

