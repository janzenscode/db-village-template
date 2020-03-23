from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.index),
    path('tambah_pendidikan/', views.addPendidikan),
    path('mengubah_pendidikan/', views.editPendidikan),
    path('menghapus_pendidikan/', views.hapusPendidikan),
]

