from django.shortcuts import render, redirect
from .forms import UserLoginForm
from .services.services import login_account, logout_account

def auth(request):
    data = {}
    form = UserLoginForm()

    if request.method == 'POST':
        if login_account(request):
            return redirect('main')
        else:
            data['form_error'] = 'Invalid data'
            form = UserLoginForm(data=request.POST)


    data['form'] = form
    return render(request, 'users/auth.html', data)

def logout(request):
    logout_account(request)
    return redirect('main')

def registration(request):
    pass