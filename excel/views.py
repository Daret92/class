from django.shortcuts import render
from users.models import CustomUserProveedor
from .forms import UploadProductForm
from django.http import HttpResponseBadRequest
from django.template import RequestContext
import django_excel as excel
from pyexcel_xlsx import get_data
import json
# Create your views here.
def uploadFile(request,token):
    user = CustomUserProveedor.objects.filter(token_upload=token).first()
    if user:
        form = UploadProductForm()
        obj = None
        pk=None
        if request.method == "POST":
            form = UploadProductForm(request.POST, request.FILES)
            if form.is_valid():
                filehandle = get_data(request.FILES['fileUp'])
                
                for i in range(len(filehandle["Hoja 1"])):
                    if i == 0:
                        print("Cabecera del excel")
                        for subItem in filehandle["Hoja 1"][i]:
                            print(subItem)
                        

                    else:
                        print("Informacion")
                        print(filehandle["Hoja 1"][i])
                

            else:
                return HttpResponseBadRequest()
        context={
            "obj":obj,
            "pk":pk,
            "form":form
        }
        return render(request,'uploadFile.html',context)
    else:
        return render(request,'404None.html')

