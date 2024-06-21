from django.shortcuts import render
from django.urls import path

from try1.models import Package

def index(request):
    
    current_user=request.user
    pack=Package.objects.all()
    

    return render(request, 'index.html',{'pack':pack,'user':current_user}
       
    )
