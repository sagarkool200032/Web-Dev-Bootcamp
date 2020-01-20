from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<em>My Second Project</em>")

def help(request):
    newDict = {"namePage":"This is the HELP Page"}
    return render(request,"proTwo/help.html",context=newDict)
