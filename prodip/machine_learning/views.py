from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def machine(request):
    return HttpResponse ('Welcome to django project. This is my first django project. Thank you :)')
