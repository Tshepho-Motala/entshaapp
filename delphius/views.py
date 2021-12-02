from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponseRedirect
import calendar
from  calendar import HTMLCalendar
from .models import *
from .forms import *
from datetime import datetime


# Create your views here.

def add_project(request):
    submitted = False
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/delphius/add_project?submitted=True')
    else:
        form = ProjectForm
        if 'submitted' in request.GET:
            submitted = True       
    return render(request, 'delphius/add_projects.html', {'form':form, 'submitted':submitted})

def add_validation(request):
    submitted = False
    if request.method == "POST":
        form = ValidationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/delphius/add_validation?submitted=True')
    else:
        form = ValidationForm
        if 'submitted' in request.GET:
            submitted = True       
    return render(request, 'delphius/add_validation.html', {'form':form, 'submitted':submitted})


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

def show_forms(request):

    return render(request, 'delphius/forms.html', {})    

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


def view_project(request):
    view_project = New_Project.objects.all()
    return render(request, 'delphius/projects.html', {'view_project':view_project})   

def update_project(request, New_Project_id):
    new_project = New_Project.objects.get(pk=New_Project_id)
    form = ProjectForm(request.POST or None, instance=new_project)
    if form.is_valid():
        form.save()
        return redirect('view-project')
    return render(request, 'delphius/update_project.html', {'new_project':new_project, 'form': form})  

def show_project(request, New_Project_id):
    new_project = New_Project.objects.get(pk=New_Project_id)    
    return render(request, 'delphius/show_projects.html', {'new_project':new_project})   


def show_validation(request, New_Validation_id):
    new_validation = New_Validation.objects.get(pk=New_Validation_id)    
    return render(request, 'delphius/show_validation.html', {'new_validation':new_validation})    

def view_validation(request):
    view_lead = New_Validation.objects.all()
    return render(request, 'delphius/validations.html', {'view_validation':view_validation})  

def update_validation(request, New_Validation_id):
    new_validation = New_Validation.objects.get(pk=New_Validation_id)
    form = ValidationForm(request.POST or None, instance=new_validation)
    if form.is_valid():
        form.save()
        return redirect('view-validation')
    return render(request, 'delphius/update_validation.html', {'new_validation':new_validation, 'form': form})                       