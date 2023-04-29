from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpRequest,HttpResponse,HttpResponseRedirect
# Create your views here.
# tasks=[]

class NewForm(forms.Form):
    task=forms.CharField(label="New Task")
def index1(requests):
    if "tasks" not in requests.session:
        requests.session["tasks"]=[]
    return render(requests, 'tasks/new.html',{
        "tasks":requests.session["tasks"]
    })

def add(requests):
    if requests.method=="POST":
        form=NewForm(requests.POST)
        if form.is_valid():
            task=form.cleaned_data['task']
            requests.session["tasks"]+=[task]
            return HttpResponseRedirect(reverse('tasks:index1'))
        else:
            return render(requests, 'tasks/add.html',{
                "form":form
            })

        # task.cleaned_data['task']
        # tasks.append(task)
    return render(requests, 'tasks/add.html',{
        "form":NewForm()
    })