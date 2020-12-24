import django
from django.shortcuts import render,redirect
from django.http import JsonResponse
def index(request):
    variable={
        "variable": "Hola Mundo desde Back"
    }
    return JsonResponse({'success':True,'mensaje':"Guardado Correctamente"})
