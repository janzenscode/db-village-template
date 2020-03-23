from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'title':'Kepala Keluarga',
    }
    return render(request,'kepala_keluarga/kepala_keluarga.html',context)

def addKepala_Keluarga(request):
    context = {
        'title':'Kepala Keluarga',
    }
    return render(request,'kepala_keluarga/tambah_kepala_keluarga.html',context)

def editKepala_Keluarga(request):
    context = {
        'title':'Kepala Keluarga',
    }
    return render(request,'kepala_keluarga/ubah_kepala_keluarga.html',context)

def hapusKepala_Keluarga(request):
    context = {
        'title':'Kepala Keluarga',
    }
    return render(request,'kepala_keluarga/hapus_kepala_keluarga.html',context)