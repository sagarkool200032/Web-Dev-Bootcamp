from django.shortcuts import render
from django.http import HttpResponse
from firstApp.models import Topic,Webpage,AccessRecord

# Create your views here.

def index(request):
    webpageList = AccessRecord.objects.order_by("date")
    date_dict = {"accessRecords" : webpageList}
    return render(request,"firstApp/index.html",context=date_dict)

def newPage(request):
    return HttpResponse("NEW PAGE")
