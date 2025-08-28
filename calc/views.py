from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# def home(request):
#     return HttpResponse("<h1>Hello world</h1>")

def home(request):
    return render(request, 'home.html')

def numerical(request):

    val1=int(request.POST["num1"])
    val2=int(request.POST["num2"])
    sum= val1+val2
    diff=val1-val2

    res=[sum,diff]
    return render(request, 'request.html',{'sum':sum,'diff':diff,'res':res})