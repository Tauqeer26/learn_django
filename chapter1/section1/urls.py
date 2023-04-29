from django.urls import path
from . import views

urlpatterns=[
    path("",views.index,name="index"),
    #path("<str:name>",views.harry,name="harry"),
    path("ht",views.http,name="http"),
    path("<str:course>",views.index_1,name="new"),
]