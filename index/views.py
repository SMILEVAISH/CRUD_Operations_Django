
from urllib.robotparser import RequestRate
from django.shortcuts import render,redirect 
from index.forms import UserForm
from .models import User


def index(request):
    objects = User.objects.all()
    return render(request,'index.html',{'d':objects})

# Create
def create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        return redirect('create')
    else:
        form = UserForm
    c = { 'form' : form }
    return render(request,'create.html',c)

# Update
def update(request,id):
    obj = User.objects.get(id=id)
    if request.method == "POST":
        form = UserForm(request.POST , instance=obj)
        if form.is_valid():
            form.save()
            return redirect('read')
        return redirect('update')    
    else:
        form = UserForm        
    context = {
        'form':form
    }
    return render(request,'update.html',context)

# Delete
def delete(request,id):
    obj = User.objects.get(id = id)
    obj.delete()
    return render(request,'delete.html',{'data':obj})
