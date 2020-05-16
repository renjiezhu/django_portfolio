from django.shortcuts import render

# Create your views here.


def homepage(request):
    context = {
        
    }
    return render(request, 'portfolio/index.html', context)

def project_page(request):
    context = {
        
    }
    return render(request, 'portfolio/index.html', context)

def contact_page(request):
    context = {
        
    }
    return render(request, 'portfolio/index.html', context)