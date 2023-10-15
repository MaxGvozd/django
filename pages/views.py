from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def show1(request):
    return render(request, 'index.html')


def show2(request):
    return HttpResponse("Page2")


def show3(request):
    return HttpResponse("Page3")
