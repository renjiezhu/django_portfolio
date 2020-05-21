from django.shortcuts import render
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        # using the post submit data to create a form
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.changed_data.get('username')
            messages.success(request, f'Accounted created for {username}')
            return redirect('todo_main_page')
    else:
        form = UserRegisterForm()
       
    context = {
        'form': form,
    }
    
    return render(request, 'users/register.html', context)


def login(request):

    context = {

    }
    return render(request, 'users/login.html', context)
