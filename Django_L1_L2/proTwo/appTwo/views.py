from django.shortcuts import render
from django.http import HttpResponse
from appTwo.models import User

# Create your views here.
def index(request):
    return HttpResponse("<em>My Second Project</em>")

def help(request):
    newDict = {"namePage":"This is the HELP Page"}
    return render(request,"proTwo/help.html",context=newDict)

def showData(request):
    datalist = User.objects.order_by("fName")
    dataDict = {"containData" : datalist}
    return render(request,"proTwo/data.html",context = dataDict)

def showUser(request):
    datalist = User.objects.order_by("fName")
    dataDict = {"containData" : datalist}
    return render(request,"proTwo/users.html",context = dataDict)

