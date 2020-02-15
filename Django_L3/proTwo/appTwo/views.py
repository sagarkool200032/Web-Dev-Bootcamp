from django.shortcuts import render
# from django.http import HttpResponse
# from appTwo.models import User
from appTwo.forms import NewUserForm


# Create your views here.
def index(request):
    return render(request,"appTwo/index.html")

def help(request):
    newDict = {"namePage":"This is the HELP Page"}
    return render(request,"appTwo/help.html",context=newDict)

# def showData(request):
#     datalist = User.objects.order_by("fName")
#     dataDict = {"containData" : datalist}
#     return render(request,"appTwo/data.html",context = dataDict)

def users(request):
    # datalist = User.objects.order_by("fName")
    # dataDict = {"containData" : datalist}
    # return render(request,"proTwo/users.html",context = dataDict)

    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("error form is invalid")

    return render(request,"appTwo/users.html",{"form":form})
