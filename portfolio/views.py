from django.shortcuts import render

from .models import *

# Create your views here.


def homepage(request):
    context = {
        
    }
    return render(request, 'portfolio/index.html', context)

def project_page(request):

    work_exp = Experience.objects.filter(experience_type='work')
    proj_exp = Experience.objects.filter(experience_type='project')

    context = {
        'title': 'Projects',
        'work_exp': work_exp,
        'proj_exp': proj_exp
    }
    return render(request, 'portfolio/experience.html', context)

def contact_page(request):
    context = {
        'title': 'Contacts',
    }
    return render(request, 'portfolio/contacts.html', context)
