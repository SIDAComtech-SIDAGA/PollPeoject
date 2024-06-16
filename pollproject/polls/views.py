from django.shortcuts import render
from .models import Choice, Question

# Get Question and Display them

def index(request):
    return render(request='polls/index.html')
