from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='authentication:login')
def index(req):
    return render(req, 'contacts/index.html')