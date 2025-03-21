#from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    #return HttpResponse("home page")
    return render(request, 'base.html')

def about(request):
    #return HttpResponse("about page")
    return render(request, 'about.html')