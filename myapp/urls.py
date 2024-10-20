# myapp/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # Ensure this template exists
