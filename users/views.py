import django
from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from product.models import ProductInventory

@login_required(login_url='/accounts/login/')
def index(request):
    obj = ProductInventory.objects.all()
    context={
        "variable": obj
    }
    return render(request,'index.html',context)

def addCar(request):
    print(request.GET)
    return JsonResponse({'success':True,'mensaje':"Ocurrio un error al iniciar sesion"})

def logoutUser(request):
    logout(request)
    return redirect("/")