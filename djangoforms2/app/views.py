from django.shortcuts import render
from app.forms import *
from app.models import *
from django.http import HttpResponse

# Create your views here.

def insert_student(request):
    SFD=Studentform()
    d={'SFD':SFD}
    if request.method=='POST':
        SFO=Studentform(request.POST)
        if SFO.is_valid():
            sid=SFO.cleaned_data['sid']
            sname=SFO.cleaned_data['sname']
            email=SFO.cleaned_data['email']
            SO=Student.objects.get_or_create(sid=sid,sname=sname,email=email)[0]
            SO.save()
            SF=Student.objects.all()
            d1={'SF':SF}
        return render(request,'display.html',d1)
    return render(request,'student.html',d)