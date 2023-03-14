
from django.urls import path
from .import  views

urlpatterns=[
     path('',views.home, name='index'),
     path('category-list',views.category_list,name='categories'),
     path('listings',views.ListingsView.as_view(),name='listings'),
     path('category-listings/<int:cat_id>',views.category_listings,name='category-listings'),
     path('listing/<str:slug>/<int:id>', views.listing_detail, name='listing'),
     path('tenancy/',views.tenancy,name='tenancy'),
     # path('listings/<str:type>/', views.tenancy_listings_view, name='listings'),
     path('<str:type_name>/', views.tenancy_listings_view, name='listings_by_type'),

]

