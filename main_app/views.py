from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return HttpResponse("<h1>Yo yo it's neopets<h1>")

def about(request):
    return render(request,"about.html")

def neopets_index(request):
    return render(request, 'neopets/index.html', {'neopets': neopets })
# Classes
class Neopet:
    def __init__(self, name, species, gender, temperament):
        self.name = name
        self.species = species
        self.gender = gender
        self.temperament = temperament

neopets = [
    Neopet('Slatty', 'Skeith', 'Male', 'Very Friendly'),
    Neopet('Litty', 'Grundo', 'Male', 'Dim-witted but good hearted'),
]