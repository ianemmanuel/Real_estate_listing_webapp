from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView, UpdateView, DeleteView
from .form import CustomerSignUpForm, EmployeeSignUpForm, EditSettingsForm, PasswordChangingForm, ProfilePageForm, EditProfilePageForm
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm,  PasswordChangeForm
from django.contrib.auth.views import  PasswordChangeView
from .models import User, Profile
from listings.models import Listing, Category
from listings.forms import ListingForm, UpdateListingForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, CreateView, ListView

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
    form_class = EditSettingsForm
    template_name = 'user/settings.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        return self.request.user
    

class PasswordsChangeView(PasswordChangeView):
  form_class = PasswordChangingForm
  # form_class = PasswordChangeForm
  success_url = reverse_lazy('password_success')
  # success_url = reverse_lazy('login')

def password_success(request):
  return render(request, 'user/password_success.html',{})


class ShowProfilePageView(DetailView):
  model = Profile
  template_name = 'user/user_profile.html'

  def get_context_data(self, *args, **kwargs):
    # users = Profile.objects.all()
    context = super(ShowProfilePageView, self).get_context_data(*args,**kwargs)
    page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
    context["page_user"] = page_user
    return context

class EditProfilePageView(generic.UpdateView):
  model = Profile
  template_name = 'user/edit_profile_page.html'
  form_class =  EditProfilePageForm

  success_url = reverse_lazy('index')

class CreateProfilePageView(CreateView):
  model = Profile
  template_name = 'user/create_user_profile_page.html'
  form_class = ProfilePageForm
  success_url = reverse_lazy('index')


  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)
  
class ViewListings(ListView):
	model = Listing
	template_name = 'dashboard/my_listings.html'