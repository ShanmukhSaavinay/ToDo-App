from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.
def index(request):
    all_works = Work.objects.all()

    form = WorkForm()

    if request.method == "POST":
        form = WorkForm(request.POST)
        if form.is_valid() :
            form.save()
        return redirect('/')
    con = {'works' : all_works , 'forms' : form }
    return render(request,'works/index.html',con)

def UpdateWork(request,primary_key):
    task = Work.objects.get(id = primary_key)
    form = WorkForm(instance=task)

    if request.method == "POST" :
        form = WorkForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'works/update_work.html',{'form' : form})

def delete_item(request,primary_key) :
    item = Work.objects.get(id = primary_key)

    if request.method == "POST":
        item.delete()
        return redirect('/')
    return render(request,'works/delete_confirm.html',{'item' : item})
