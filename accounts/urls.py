from django.urls import path
from .import  views
from django.contrib.auth import views as  auth_views

urlpatterns=[
     path('register/',views.register, name='register'),
     path('customer_register/',views.customer_register.as_view(), name='customer_register'),
     path('employee_register/',views.employee_register.as_view(), name='employee_register'),
     path('login/',views.login_request, name='login'),
     path('logout/',views.logout_view, name='logout'),
     path('my-dashboard',views.my_dashboard, name='my_dashboard'),
     path('add-listing', views.AddListingView.as_view(), name='add_listing'),
     path('update-listing/edit/<int:pk>', views.UpdateListingView.as_view(), name='update_listing'),
     path('delete-listing/delete/<int:pk>', views.DeleteListingView.as_view(), name='delete_listing'),
     path('settings/',views.UserEditView.as_view(), name='settings'),
     path('password/', views.PasswordsChangeView.as_view(template_name ="user/change-password.html")),
     path('password_success', views.password_success, name="password_success"),
]