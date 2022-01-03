# Create your views here.
from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

class Tiger:
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

tigers = [
  Tiger('Siber', 'Bengal', 'Likes to play', 5),
  Tiger('Ginger', 'Siberian', 'Enjoys running', 2),
  Tiger('Sharp', 'Caspian', 'Very lazy, and enjoys swimming', 3),
  Tiger('Big Man', 'Sumatran', 'Very grumpy', 8)
]


# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def tigers_index(request):
  return render(request, 'tigers/index.html', {'tigers': tigers})