from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse
def django_forms(request):
    formobject=student_Forms
    d={'form':formobject}
    if request.method=='POST':
        FD=student_Forms(request.POST)
        if FD.is_valid():
            n=FD.cleaned_data['name']
            a=FD.cleaned_data['age']
            e=FD.cleaned_data['email']
            d1={'n':n,'a':a,'e':e}
            return render(request,'forms_data.html',d1)
        
        
    return render(request,'django_forms.html',d)