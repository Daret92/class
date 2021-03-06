import django
from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from product.models import ProductInventory,Product
from users.models import productsCarUser,carUser
from django.contrib import messages
from decimal import *
from .forms import SignUpForm,UpdateUpForm,PasswordForm
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User

@login_required(login_url='/accounts/login/')
def index(request):
    obj = ProductInventory.objects.all()
    carrito = carUser.objects.filter(user=request.user,is_pendient=True).first()
    if carrito:
        productos = productsCarUser.objects.filter(carUser=carrito)
    else:
        productos = None

    context={
        "variable": obj,
        "carrito":carrito,
        "productos":productos
    }
    return render(request,'index.html',context)

def newUser(request):
    form = SignUpForm()
    if request.method == "POST":
        print(request.POST)
        if form.is_valid():
            print(form)
    context={
        'form':form
    }
    return render(request,'registration/registro.html',context)

def editUser(request):
    form = PasswordForm()
    if request.method == "POST":
        form = PasswordForm(request.POST)
        if form.is_valid():
           if check_password(request.POST['contraseña_actual'],request.user.password):
               request.user.set_password(request.POST["confirma_la_contraseña"])
    context = {
        "form":form
    }
    return render(request,'user/editUser.html', context)

def addCar(request):
    try:
        carrito = carUser.objects.filter(user=request.user,is_pendient=True)
        productoTmp = Product.objects.get(pk=request.GET.get("pk_product"))
        stock = ProductInventory.objects.get(pk=request.GET.get("pk_product"))

        if len(carrito) > 0:
            productoCarrito = productsCarUser.objects.filter(carUser=carrito.first(),product=productoTmp).first()

            if productoCarrito:
                productinventory = ProductInventory.objects.get(pk=request.GET.get("pk_product"))
                productoCarrito.total = productoCarrito.total+float(request.GET.get("total_product"))
                if stock.stock >= productoCarrito.total:
                    productoCarrito.save()
                    #messages.add_message(request,messages.INFO,"Agregado a tu carrito")
                else:
                    #messages.add_message(request,messages.INFO,"Tu pedido supero nuestro Stock")
                    return  JsonResponse({'success':False,'mensaje':"Tu pedido supero nuestro stock"})

                return  JsonResponse({'success':True,'mensaje':"Agregado al carrito","pk_producto":productoCarrito.id,"name":productoCarrito.product.name,"total":productoCarrito.total})
            else:
                productoCarrito = productsCarUser.objects.create(carUser=carrito.first(),product=productoTmp,total=request.GET.get("total_product"))
            return JsonResponse({'success':True,'mensaje':"Agregado al carrito","pk_producto":productoCarrito.id,"name":productoCarrito.product.name,"total":productoCarrito.total})
        else:
            carrito = carUser.objects.create(user=request.user)
            productoCarrito = productsCarUser.objects.create(carUser=carrito,product=productoTmp,total=request.GET.get("total_product"))
            return JsonResponse({'success':True,'mensaje':"Agregado al carrito","pk_producto":productoCarrito.id,"name":productoCarrito.product.name,"total":productoCarrito.total})
    except Exception as e:
        print(e)
        return JsonResponse({'success':False,'mensaje':"Ocurrio un error al integrar al carrito"})

def logoutUser(request):
    logout(request)
    messages.add_message(request,messages.INFO,"Sesion Cerrada")
    return redirect("/")


def customUser(request):
    form = UpdateUpForm(instance=request.user)
    if request.method == "POST":
        form = UpdateUpForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.WARNING, "Usuario Actualizado")
    context= {
        "form":form
    }
    return render(request,"user/custom.html",context)
<<<<<<< HEAD
=======

def editUser(request):
    form = PasswordForm()
    if request.method == "POST":
        form = PasswordForm(request.POST)
        if form.is_valid():
           if check_password(request.POST['contraseña_actual'],request.user.password):
               request.user.set_password(request.POST["confirma_la_contraseña"])
               messages.add_message(request,messages.INFO, "Contraseña Actualizada")
    context = {
        "form":form
    }
    return render(request,'user/editUser.html', context)
>>>>>>> 18c24a6c98d2785d54aca58d5fadc892b0fc3abe
