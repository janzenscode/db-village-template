from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'title':'PENGGUNA',
    }
    return render(request,'pengguna/pengguna.html',context)

def addPengguna(request):
    context = {
        'title':'PENGGUNA',
    }
    return render(request,'pengguna/tambah_pengguna.html',context)

def editPengguna(request):
    context = {
        'title':'PENGGUNA',
    }
    return render(request,'pengguna/ubah_pengguna.html',context)

def deletePengguna(request):
    context = {
        'title':'PENGGUNA',
    }
    return render(request,'pengguna/hapus_pengguna.html',context)