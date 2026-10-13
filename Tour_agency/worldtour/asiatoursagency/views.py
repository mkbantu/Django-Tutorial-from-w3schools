from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import tour

def index(request):
    mytours = tour.objects.all()
    return render(request, 'asia/index.html', {'mytours': mytours})