from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from contacts.models import Contact

from .forms import RegisterForm, LoginForm

def register(req):
    if req.method == 'POST':
        form = RegisterForm(req.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            Contact.objects.create(owner=user, is_owner=True, first_name=user.first_name, last_name=user.last_name)

            return redirect('authentication:login')
    
    else:
        form = RegisterForm()
    
    return render(req, 'authentication/register.html', { 'form': form })

def login(req):
    if req.method == 'POST':
        form = LoginForm(req.POST)

        if form.is_valid():
            user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])

            if user is not None:
                auth_login(req, user)

                if not form.cleaned_data.get('remember_me'):
                    req.session.set_expiry(0)

                next_url = req.GET.get('next', 'contacts:index')

                return redirect(next_url)
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
        
    return render(req, 'authentication/login.html', { 'form': form })

def logout(req):
    auth_logout(req)

    return redirect('authentication:login')