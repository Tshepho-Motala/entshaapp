from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponseRedirect
from .models import *
from .forms import JobForm
from datetime import datetime


# Create your views here.
def NGBS_home(request):
    """Renders the NGBS page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'NGBS/index.html',
        {
            'title':'NGBS Page',
            'year':datetime.now().year,
        }
    )



def job_list(request):
    context = {'job_list': JobCart.objects.all() }
    return render(request, "NGBS/job_list.html", context )

def job_form(request):
    if request.method == "GET":
        form = JobForm()
        return render(request, "NGBS/job_form.html", {'form':form})
    else:
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/NGBS/list')

