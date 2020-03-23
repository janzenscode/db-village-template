from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'title':'PEKERJAAN',
    }
    return render(request,'pekerjaan/pekerjaan.html',context)

def addPekerjaan(request):
    context = {
        'title':'PEKERJAAN',
    }
    return render(request,'pekerjaan/tambah_pekerjaan.html',context)

def editPekerjaan(request):
    context = {
        'title':'PEKERJAAN',
    }
    return render(request,'pekerjaan/ubah_pekerjaan.html',context)

def hapusPekerjaan(request):
    context = {
        'title':'PEKERJAAN',
    }
    return render(request,'pekerjaan/hapus_pekerjaan.html',context)