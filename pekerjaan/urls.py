from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.index),
    path('tambah_pekerjaan/', views.addPekerjaan),
    path('mengubah_pekerjaan/', views.editPekerjaan),
    path('menghapus_pekerjaan/', views.hapusPekerjaan),
]

