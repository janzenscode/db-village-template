from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index),
    path('tambah/', views.addPengguna),
    path('mengubah/', views.editPengguna),
    path('menghapus/', views.deletePengguna),
]