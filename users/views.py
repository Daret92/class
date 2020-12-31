import django
from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from product.models import ProductInventory,Product
from users.models import productsCarUser,carUser
from decimal import Decimal

@login_required(login_url='/accounts/login/')
def index(request):
    obj = ProductInventory.objects.all()
    context={
        "variable": obj
    }
    return render(request,'index.html',context)

def addCar(request):
    try:
        carrito = carUser.objects.filter(user=request.user,is_pendient=True)
        productoTmp = Product.objects.get(pk=request.GET.get("pk_product"))
        if len(carrito) > 0:
            productoCarrito = productsCarUser.objects.filter(carUser=carrito.first(),product=productoTmp).first()
            if productoCarrito:
                productoCarrito.total = productoCarrito.total+Decimal(request.GET.get("total_product"))
                productoCarrito.save()
            else:
                productoCarrito = productsCarUser.objects.create(carUser=carrito.first(),product=productoTmp,total=request.GET.get("total_product"))
            return JsonResponse({'success':True,'mensaje':"Agregado al carrito"})
        else:
            carrito = carUser.objects.create(user=request.user)
            productoCarrito = productsCarUser.objects.create(carUser=carrito,product=productoTmp,total=request.GET.get("total_product"))
            return JsonResponse({'success':True,'mensaje':"Agregado al carrito"})
    except Exception as e:
        print(e)
        return JsonResponse({'success':False,'mensaje':"Ocurrio un error al integrar al carrito"})

def logoutUser(request):
    logout(request)
    return redirect("/")