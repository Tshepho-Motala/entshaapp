from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponseRedirect
import calendar
from  calendar import HTMLCalendar
from .models import *
from .forms import *
from datetime import datetime


# Create your views here.

def add_lead(request):
    submitted = False
    if request.method == "POST":
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/delphius/add_lead?submitted=True')
    else:
        form = LeadForm
        if 'submitted' in request.GET:
            submitted = True       
    return render(request, 'delphius/add_lead.html', {'form':form, 'submitted':submitted})

def delphius_home(request):
    
    return render(request,
     'delphius/index.html', {  

        })  

def show_lead(request, New_Lead_id):
    new_lead = New_Lead.objects.get(pk=New_Lead_id)    
    return render(request, 'delphius/show_leads.html', {'new_lead':new_lead})    

def view_lead(request):
    view_lead = New_Lead.objects.all()
    return render(request, 'delphius/leads.html', {'view_lead':view_lead})  

def update_lead(request, New_Lead_id):
    new_lead = New_Lead.objects.get(pk=New_Lead_id)
    form = LeadForm(request.POST or None, instance=new_lead)
    if form.is_valid():
        form.save()
        return redirect('view-lead')
    return render(request, 'delphius/update_lead.html', {'new_lead':new_lead, 'form': form})        