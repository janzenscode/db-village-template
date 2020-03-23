from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'title':'PENDIDIKAN',
    }
    return render(request,'pendidikan/pendidikan.html',context)

def addPendidikan(request):
    context = {
        'title':'PENDIDIKAN',
    }
    return render(request,'pendidikan/tambah_pendidikan.html',context)

def editPendidikan(request):
    context = {
        'title':'PENDIDIKAN',
    }
    return render(request,'pendidikan/ubah_pendidikan.html',context)

def hapusPendidikan(request):
    context = {
        'title':'PENDIDIKAN',
    }
    return render(request,'pendidikan/hapus_pendidikan.html',context)