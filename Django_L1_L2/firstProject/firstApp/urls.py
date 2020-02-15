from django.conf.urls import url
from firstApp import views


urlpatterns = [
    url(r"^$",views.newPage,name="index")
]
