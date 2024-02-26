from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest

@login_required(login_url='authentication:login')
def index(req: HttpRequest):
    user_contacts = req.user.contacts.all().filter(is_owner = False)

    return render(req, 'contacts/index.html', { 'user_contacts': user_contacts })