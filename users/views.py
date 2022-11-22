from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.

def register(request):
    """register new user"""
    if request.method != 'POST':
        # shows empty form
        form = UserCreationForm()
    else:
        # perform filed form
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()

            # login and redirect to home
            login(request, new_user)
            return redirect('web_notes:index')

    # shows empty or incorrect form
    context = {'form': form}
    return render(request, 'registration/register.html', context)

