from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from . models import Product
from . forms import MakePost

def index(request):
    product = Product.objects.all()
    contex = {
        'post':product
    }
    return render(request,"index.html",contex)
@login_required
def product(request):
    form=product()
    if request.method == 'POST':
        form = product(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form=product()
            return render(request,"post.html",{"form":form})
def singup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("singup")
    return render(request,"singup.html",{"form":form})
def addproduct(request):
    form = MakePost()
    if request.method == 'POST':
        form = MakePost(request.POST)
        if form.is_valid():
            form.save()
            return redirect("addproduct")
    return render(request,"addproduct.html",{"form":form})


    