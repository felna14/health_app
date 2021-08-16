from django.http import request
from django.shortcuts import render, get_object_or_404


# Create your views here.
from health_lab.models import Doctor,Dept


def DeptDetail(request,c_slug=None):
    c_page=None
    doctor=None
    if(c_slug!=None):
        c_page=get_object_or_404(Dept,slug=c_slug)
        doctor=Doctor.objects.filter(dept=c_page)
    else:
        doctor = Doctor.objects.all().filter()
    return render(request,'home.html',{'dept':c_page,'doctor':doctor})


def DocDetail(reuest,c_slug,doctor_slug):
    try:
        doc=Doctor.objects.get(dept__slug=c_slug,slug=doctor_slug)
    except Exception as e:
        raise e
    return render(reuest,'detail.html',{'doc':doc})

