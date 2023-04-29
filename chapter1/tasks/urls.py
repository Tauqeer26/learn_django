from django.urls import path
from . import views

app_name="tasks"
urlpatterns=[
    path("",views.index1,name="index1"),
    path("add",views.add,name="add"),
]