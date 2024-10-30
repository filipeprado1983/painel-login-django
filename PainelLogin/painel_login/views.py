from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# View para login
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redireciona após login
        else:
            messages.error(request, 'Usuário ou senha inválidos')
    return render(request, 'login.html')  # Renderiza o template de login

# View para logout
def logout_view(request):
    logout(request)
    return redirect('login')  # Redireciona para a página de login após o logout

# View para home
def home_view(request):
    return render(request, 'home.html')  # Renderiza o template de home
