from django.contrib.auth import login, logout, authenticate
from ..forms import UserLoginForm
from ..models import User

def login_account(request) -> bool:
    form = UserLoginForm(data=request.POST)
    if form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return True
        return False
    

def logout_account(request) -> None:
    logout(request)
    return None

