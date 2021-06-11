from django.shortcuts import render
from pessoa.models import Pessoa
from pessoa.forms import LoginForm

# Create your views here.
def login(request):
    data = {}
    data['form'] = LoginForm()
    return render(request, 'login.html', data)