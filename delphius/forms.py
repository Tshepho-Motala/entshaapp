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
        fields = ('site', 'cont_person', 'cont_no', 'address', 'region', 'status', 'employee', 'started', 'expected', 'verified', 'action', 'latitude', 'longitude', 'lead_image')

        labels = {

            'site': '',
            'cont_person': '',
            'cont_no': '',
            'address': '',
            'region': '',
            'status': 'Lead status',
            'employee': 'Lead brought by',
            'started': '',
            'expected': '',
            'verified': '',
            'action': '',
            'latitude': '',
            'longitude': '',
            'lead_image': '',



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
            'latitude': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the latitude'}),
            'longitude': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the longitude'}),
            #'lead_image': forms.ImageField(attrs={'class': 'form-control', 'placeholder': 'Choose an image'}),

        }


class ProjectForm(ModelForm):
    class Meta:
        model = New_Project
        fields = ('status', 'employee', 'started', 'expected', 'verified', 'action', 'site', 'cont_person', 'cont_no', 'address', 'region',   'latitude', 'longitude', 'lead_image')

        labels = {

            'status': 'Lead status',
            'employee': 'Lead brought by',
            'started': '',
            'expected': '',
            'verified': '',
            'action': '',
            'site': '',
            'cont_person': '',
            'cont_no': '',
            'address': '',
            'region': '',
            'latitude': '',
            'longitude': '',
            'lead_image': '',



        }
        widgets = {

            'status': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select the status'}),
            'employee': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select the employee'}),
            'started': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Enter the date started'}),
            'expected': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Enter the date expected'}),
            'verified': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Enter the date verified'}),
            'action': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Enter the date for action'}),
            'site': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your site'}),
            'cont_person': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter contacts person name'}),
            'cont_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter person number'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the address'}),
            'region': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the region'}),    
            'latitude': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the latitude'}),
            'longitude': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the longitude'}),
            #'lead_image': forms.ImageInput(attrs={'class': 'form-control', 'placeholder': 'Choose an image'}),

        }


class ValidationForm(ModelForm):
    class Meta:
        model = New_Validation
        fields = ('site', 'cont_person', 'cont_no', 'address', 'region', 'latitude', 'longitude', 'solution_type', 'est_duration', 'ppr', 'ppl', 'mar', 'est_municipal', 'pce', 'dawn_dusk', 'dci', 'ss', 'esc', 'oi', 'lead_image')

        labels = {

            'site': '',
            'cont_person': '',
            'cont_no': '',
            'address': '',
            'region': '',
            'latitude': '',
            'longitude': '',
            'solution_type': '',
            'est_duration': '',
            'ppr': 'Public Participation Required',
            'ppl': 'Public Participation Likelihood',
            'mar': 'Municipal Approval Required',
            'est_municipal': '',
            'pce': '',
            'dawn_dusk': ' Dawn to Dusk Estimate',
            'dci': 'Del Connect Estimate ',
            'ss': 'Solution Shareable ',
            'esc': '',
            'oi': 'Operator Interest',
            'lead_image': ' Attachments',



        }
        widgets = {

            'site': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your site'}),
            'cont_person': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter contacts person name'}),
            'cont_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter person number'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the address'}),
            'region': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the region'}),
            'latitude': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the latitude'}),
            'longitude': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the longitude'}),
            'est_duration': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the Duration of Public Participation'}),
            'ppr': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select the Public Participation Required'}),
            'ppl': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select the Public Participation Likelihood'}),
            'mar': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select the Municipal Approval Required'}),
            'est_municipal': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Estimated Municipal in days'}),
            'pce': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Power Connection Estimate'}),
            'dawn_dusk': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select the Dawn to Dusk Estimate'}),
            'dci': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select the Del Connect Interested'}),
            'ss': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select the Solution Shareable'}),
            'esc': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Estimated Solution Cost'}),
            'oi': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select the Operator Interest'}),
           #'lead_image': forms.ImageField(attrs={'class': 'form-control', 'placeholder': 'Choose an image'}),

        }        




