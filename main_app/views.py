# Create your views here.
from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Tiger
from .forms import FeedingForm

# Add the following import
from django.http import HttpResponse

# Define the home view
class TigerCreate(CreateView):
  model = Tiger
  fields = '__all__'
  success_url = '/cats/'

class TigerCreate(CreateView):
  model = Tiger
  fields = ['name', 'breed', 'description', 'age']

class TigerUpdate(UpdateView):
  model = Tiger
  fields = ['breed', 'description', 'age']

class TigerDelete(DeleteView):
  model = Tiger
  success_url = '/tigers/'

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def tigers_index(request):
  tigers = Tiger.objects.all()
  return render(request, 'tigers/index.html', {'tigers': tigers})

def tigers_detail(request, tiger_id):
  tiger = Tiger.objects.get(id=tiger_id)
  feeding_form= FeedingForm()
  return render(request, 'tigers/detail.html', {'tiger': tiger, 'feeding_form': feeding_form})

def add_feeding(request, tiger_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.tiger_id = tiger_id
    new_feeding.save()
  return redirect('tigers_detail', tiger_id=tiger_id)

  pass