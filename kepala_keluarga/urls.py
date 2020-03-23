from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('tambah_kepala_keluarga/', views.addKepala_Keluarga),
    path('mengubah_kepala_keluarga/', views.editKepala_Keluarga),
    path('menghapus_kepala_keluarga/', views.hapusKepala_Keluarga),
]