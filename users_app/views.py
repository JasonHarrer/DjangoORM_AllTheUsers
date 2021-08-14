from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request):
    context = { 'users': User.objects.all() }
    return render(request, 'index.html', context)
