from django.shortcuts import render
from .models import Link

def home(request):
    links = Link.objects.all()  # Get all the links from the database
    return render(request, 'home.html', {'links': links})
