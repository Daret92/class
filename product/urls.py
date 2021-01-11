from django.urls import path

from . import views

urlpatterns = [
    path('upload/xls/<str:token>',views.uploadFile)
]