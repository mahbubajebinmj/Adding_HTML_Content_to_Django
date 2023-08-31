from django.http import HttpResponse
from django.shortcuts import render


def homePage(request):
    return HttpResponse("hi")




def home(request):
    return render(request,"index.html")
