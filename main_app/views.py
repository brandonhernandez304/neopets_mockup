from django.shortcuts import render
from .models import Neopet

# Create your views here.


def home(request):
    return render(request, "home.html")

def about(request):
    return render(request,"about.html")

def neopets_index(request):
    neopets = Neopet.objects.all()
    return render(request, 'neopets/index.html', {'neopets': neopets })

def neopets_detail(request, neopet_id):
    neopet = Neopet.objects.get(id=neopet_id)
    return render(request, 'neopets/detail.html', {'neopet': neopet})

neopets = [
    Neopet('Slatty', 'Skeith', 'Male', 'Very Friendly'),
    Neopet('Litty', 'Grundo', 'Male', 'Dim-witted but good hearted'),
]