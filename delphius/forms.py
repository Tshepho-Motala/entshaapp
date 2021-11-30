from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from .models import *

class JobForm(forms.ModelForm):
    class Meta:
        model = JobCart
        fields = ('fullname', 'id_no','job_type','job_description')
        labels = {
            'fullname': 'Full Names',
            'id_no': 'Identity number',
            'job_type': 'Job type',
            'job_description': 'Job Description',
            
            }

        def __init__(self, *args, **kwargs):
         super(JobForm, self).__init__(*args, **kwargs)
         self.fields['id_no'].required = False

class LeadForm(ModelForm):
    class Meta:
        model = New_Lead
        fields = ('site', 'cont_person', 'cont_no', 'address', 'region', 'status', 'employee', 'started', 'expected', 'verified', 'action')

        labels = {

            'site': '',
            'cont_person': '',
            'cont_no': '',
            'address': '',
            'region': '',
            'status': 'Select the status',
            'employee': 'Select the employee',
            'started': '',
            'expected': '',
            'verified': '',
            'action': '',



        }
        widgets = {

            'site': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your site'}),
            'cont_person': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter contacts person name'}),
            'cont_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter person number'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the address'}),
            'region': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the region'}),
            'status': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select the status'}),
            'employee': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select the employee'}),
            'started': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Enter the date started'}),
            'expected': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Enter the date expected'}),
            'verified': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Enter the date verified'}),
            'action': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Enter the date for action'}),



        }
