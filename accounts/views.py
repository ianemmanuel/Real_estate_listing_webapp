from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView, UpdateView, DeleteView
from .form import CustomerSignUpForm, EmployeeSignUpForm
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from .models import User
from listings.models import Listing, Category
from listings.forms import ListingForm, UpdateListingForm
from django.urls import reverse_lazy
from django.views import generic

def register(request):
    return render(request, 'user/register.html')

class customer_register(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = 'user/customer_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

class employee_register(CreateView):
    model = User
    form_class = EmployeeSignUpForm
    template_name = 'user/employee_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return redirect('/')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'user/login.html',
    context={'form':AuthenticationForm()})

def logout_view(request):
    logout(request)
    return redirect('/')


# User Dashboard
def my_dashboard(request):

  return render(request,'dashboard/dashboard.html')


class AddListingView(CreateView):
    model = Listing
    form_class = ListingForm
    template_name = 'dashboard/add_listing.html' 
    # fields = "__all__"

class UpdateListingView(UpdateView):
    model = Listing
    template_name = 'dashboard/update_listing.html'
    form_class = UpdateListingForm
    # fields =  ['title','number_of_bedrooms','number_of_bathrooms','address','area_sqft','detail','price','video','type','price','category']

class DeleteListingView(DeleteView):
    model = Listing
    template_name = 'dashboard/delete_listing.html'
    success_url = reverse_lazy('index')

class UserEditView(generic.UpdateView):
    form_class = UserChangeForm
    template_name = 'user/settings.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        return self.request.user