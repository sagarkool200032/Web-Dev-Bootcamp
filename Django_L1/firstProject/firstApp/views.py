from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    myDict = {"insert_me":"Hello I am from views.py !"}
    return render(request,"firstApp/index.html",context=myDict)

def newPage(request):
    return HttpResponse("NEW PAGE")
