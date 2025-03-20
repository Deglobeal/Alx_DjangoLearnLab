from django.shortcuts import render
# from django.http import HttpResponse

def homepage(request):
    # return HttpResponse("Hello world, i am improving on django")
    return render(request, 'base.html')