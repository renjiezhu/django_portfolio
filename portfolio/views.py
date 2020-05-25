from django.shortcuts import render

from .models import *


def homepage(request):
    context = {
        
    }
    return render(request, 'portfolio/index.html', context)

def project_page(request):

    all_proj = Experience.objects.all()

    work_exp = all_proj.filter(experience_type='work')
    proj_exp = all_proj.filter(experience_type='project')
    education = all_proj.filter(experience_type='education')


    context = {
        'title': 'Projects',
        'work_exp': work_exp,
        'proj_exp': proj_exp,
        'education': education
    }
    return render(request, 'portfolio/experience.html', context)

def contact_page(request):
    context = {
        'title': 'Contacts',
    }
    return render(request, 'portfolio/contacts.html', context)
