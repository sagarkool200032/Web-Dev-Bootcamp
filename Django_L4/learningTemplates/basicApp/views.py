from django.shortcuts import render

# Create your views here.
def index(request):
    content = {"text":"this text is done using template filter","number":100}
    return render(request,"basicApp/index.html",content)

def other(request):
    return render(request,"basicApp/other.html")

def relative(request):
    return render(request,"basicApp/relativeUrl_templates.html")
