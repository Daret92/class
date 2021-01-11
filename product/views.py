from django.shortcuts import render
from product.forms import UploadProductForm
from users.models import CustomUserProveedor
# Create your views here.
def uploadFile(request,token):
    user = CustomUserProveedor.objects.filter(token_upload=token).first()
    if user:
        form = UploadProductForm()
        obj = None
        pk=None
        if request.method == "POST":
            pk="PAso al post"
            if request.POST.get("preview"):
                #Aqui precargamos el XLS para regresarlo a revisarlo
                obj = request.FILES.get("fileUp")
            #if request.POST.get("upload"):
            #    #Aqui se inserta todo a la BD
            #    form = UploadProductForm(request.POST,request.FILES)
            #    if form.is_valid():
            #        obj = form.save(commit=False)
            #        obj.user = user.user
            #        obj.save()

            #        for item in obj.fileUp:
                        #iterar para uardar

        context={
            "obj":obj,
            "pk":pk,
            "form":form
        }
        return render(request,'uploadFile.html',context)
    else:
        return render(request,'404None.html')