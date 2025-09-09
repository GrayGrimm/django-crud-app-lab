from django.shortcuts import render
from django.http import HttpResponse

class Plant:
    def __init__(self, name, variety, category):
        self.name = name
        self.variety = variety
        self.category = category

plants = [
    Plant('Green Bean', 'Contender', 'Vegeteable',),
    Plant('Summer Squash', 'Chifon squash', 'Vegetable'),
    Plant('Rosemary', 'Bush', 'Herb')
]
# Create your views here.
def home(request):
    return HttpResponse('<h1>Welcome to the Homesteaders Garden Journal</h1>')

def about(request):
    return render(request, 'about.html')

def plant_index(request):
    return render(request, 'plants/index.html', {'plants': plants})