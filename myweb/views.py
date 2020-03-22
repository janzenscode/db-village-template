from django.shortcuts import render

def index(request):
    context = {
        'title':'HOME',
    }
    return render(request,'index.html', context)

def login(request):
    context = {
        'title':'LOGIN',
    }
    return render(request,'login.html', context)