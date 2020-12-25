import django
from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required(login_url='/accounts/login/')
def index(request):
    context={
        "variable": "Hola Mundo desde Back"
    }
    return render(request,'index.html',context)

def logoutUser(request):
    logout(request)
    return redirect("/")