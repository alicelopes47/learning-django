from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import produto
from .forms import ProductForm

def home(request):
    return render(request, 'base.html', {})

def createUser(request):
    if request.method == "GET":
        return render(request, 'newUser.html', {})
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
       
    
        isUsernameTaken = User.objects.filter(username = username).first()

        if isUsernameTaken:
            return render(request, 'error-create.html')
        
        isValid = User.objects.create_user(username=username, email=email, password=senha)
        isValid.save()

        return render(request, 'success-create.html')

def loginPage (request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else: 
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username = username, password = senha)

        if user:
            login(request, user)
            return redirect(to='buyingpage')
        else:
            return render(request, 'error-login.html')
        
@login_required(login_url="/login")
def buyingPage (request):
        produtos = produto.objects.all()
        return render(request, 'buying-page.html', {'produtos': produtos})

@login_required(login_url="/login")
def newProduct (request):
    if request.method == 'GET':
        return render(request, 'createProduct.html')
    else: 
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='buyingpage')  
        else:
            form = ProductForm()
        return render(request, 'createProduct.html', {'form': form})
    
@login_required
def sair(request):
    logout(request)
    return redirect('home')