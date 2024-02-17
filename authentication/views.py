from django.shortcuts import render, redirect

from .forms import RegisterForm

def register(req):
    if req.method == 'POST':
        form = RegisterForm(req.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            return redirect('authentication:login')
    
    else:
        form = RegisterForm()
    
    return render(req, 'authentication/register.html', { 'form': form })
