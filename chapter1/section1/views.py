from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def http(request):
    return HttpResponse(request,"Great Work Keep going")

# def harry(request,name):
#     return HttpResponse(f"Exceelnt Work {name.capitalize()}  ")
def index(request):
    return render(request,"section1/index.html")
def index_1(request,course):
    return render(request,"section1/nice.html",
                  {
        "course":course.capitalize()
}
)