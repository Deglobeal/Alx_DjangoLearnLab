from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

def homepage(request):
    # return HttpResponse("Hello world, i am improving on django")
    return render(request, 'base.html')


