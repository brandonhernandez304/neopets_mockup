from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
# from django.contrib.auth import login
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Neopet, Toy
from .forms import FeedingForm
# Import the mixin for class-based views
# from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request,"about.html")

# neopets #

def neopets_index(request):
    neopets = Neopet.objects.all()
    return render(request, 'neopets/index.html', {'neopets': neopets })

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

def add_feeding(request, neopet_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.neopet_id = neopet_id
        new_feeding.save()
    return redirect('detail', neopet_id=neopet_id)

def assoc_toy(request, neopet_id, toy_id):
  # Note that you can pass a toy's id instead of the whole object
   Neopet.objects.get(id=neopet_id).toys.add(toy_id)
   return redirect('detail', cat_id=neopet_id)
# toys #

# CBV's
class NeopetCreate(CreateView):
    model = Neopet
    fields = ['name', 'species', 'temperament', 'gender']
    # success_url= '/neopets/'

class NeopetUpdate(UpdateView):
    model = Neopet
    fields = ['species', 'temperament', 'gender']

class NeopetDelete(DeleteView):
    model = Neopet
    success_url = '/neopets/'

# Toys #
class ToyCreate(CreateView):
    model = Toy
    fields = ('name', 'color')
class ToyUpdate(UpdateView):
    model = Toy
    fields = ('name', 'color')

class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'

class ToyDetail(DetailView):
    model = Toy
    template_name = 'toys/detail.html'

class ToyList(ListView):
    model = Toy
    template_name = 'toys/index.html'

# neopets = [
#     Neopet('Slatty', 'Skeith', 'Male', 'Very Friendly'),
#     Neopet('Litty', 'Grundo', 'Male', 'Dim-witted but good hearted'),
# ]