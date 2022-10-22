from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Import the mixin for class-based views
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Neopet, Toy
from .forms import FeedingForm

# Create your views here.

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request,"about.html")

# neopets #

def neopets_index(request):
    neopets = Neopet.objects.filter(user=request.user)
    return render(request, 'neopets/index.html', {'neopets': neopets })

@login_required
def neopets_detail(request, neopet_id):
    neopet = Neopet.objects.get(id=neopet_id)
    feeding_form = FeedingForm()
    # displaying unassociated toys
    toys_neopet_doesnt_have = Toy.objects.exclude(id__in = neopet.toys.all().values_list('id'))
    return render(request, 'neopets/detail.html', {
    # include the cat and feeding_form in the context
    'neopet': neopet,
    'feeding_form': feeding_form,
    'toys' : toys_neopet_doesnt_have,
  })

@login_required
def add_feeding(request, neopet_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.neopet_id = neopet_id
        new_feeding.save()
    return redirect('detail', neopet_id=neopet_id)

@login_required
def assoc_toy(request, neopet_id, toy_id):
  # Note that you can pass a toy's id instead of the whole object
   Neopet.objects.get(id=neopet_id).toys.add(toy_id)
   return redirect('detail', neopet_id=neopet_id)
# toys #

# CBV's
class NeopetCreate(LoginRequiredMixin,CreateView):
    model = Neopet
    fields = ['name', 'species', 'temperament', 'gender']
    # success_url= '/neopets/'
    def form_valid(self, form):
    # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the cat
    # Let the CreateView do its job as usual
        return super().form_valid(form)


class NeopetUpdate(LoginRequiredMixin,UpdateView):
    model = Neopet
    fields = ['species', 'temperament', 'gender']

class NeopetDelete(LoginRequiredMixin,DeleteView):
    model = Neopet
    success_url = '/neopets/'

# Toys #
class ToyCreate(LoginRequiredMixin,CreateView):
    model = Toy
    fields = ('name', 'color')
class ToyUpdate(LoginRequiredMixin,UpdateView):
    model = Toy
    fields = ('name', 'color')

class ToyDelete(LoginRequiredMixin,DeleteView):
    model = Toy
    success_url = '/toys/'

class ToyDetail(LoginRequiredMixin,DetailView):
    model = Toy
    template_name = 'toys/detail.html'

class ToyList(LoginRequiredMixin,ListView):
    model = Toy
    template_name = 'toys/index.html'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
