from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection

# Create your views here.
def index(request):
    return render(request, 'home.html')

