from django.shortcuts import render,redirect
# from .forms import SignupForm

from django.views.generic import CreateView
from userauth.models import customUser
from userauth.forms import CustomUserCreationForm

class signupview(CreateView):
    model=customUser
    form_class=CustomUserCreationForm
    success_url="index"
    template_name='reg.html'








def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/')
    else:
        form = CustomUserCreationForm()

    return render(request, 'reg.html', {
        'form': form
    })
