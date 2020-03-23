from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'title':'PENGATURAN',
    }
    return render(request,'pengaturan/pengaturan_umum.html',context)


def editPengaturan(request):
    context = {
        'title':'PENGATURAN',
    }
    return render(request,'pengaturan/ubah_pengaturan_umum.html',context)

