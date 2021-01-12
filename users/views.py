import django
from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from product.models import ProductInventory,Product
from users.models import productsCarUser,carUser
from django.contrib import messages
from decimal import *
from .forms import SignUpForm

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
    newform = newForm()
    if request.method == "POST":
        if form.is_valid():
            print(form)
    context={
        'form':form
    }
    return render(request,'registration/registro.html',context)
    
def editUser(request):
    return render(request,'editUser.html')

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
