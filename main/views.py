from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,logout,login
from .models import User,Posts
from .forms import UserRegisterForm,CreatePost
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/login')
def home(request):
    context = {'posts':Posts.objects.all}
    return render(request, 'home.html', context)
@login_required(login_url='/login')
def logoutview(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('home')
    context = {'form':UserRegisterForm()}
    return render(request, 'register.html', context)
@login_required(login_url='/login')
def postsomething(request):
    if request.method == 'POST':
        form = CreatePost(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('home')
    context = {'form':CreatePost()}
    return render(request, 'postsomething.html', context)

def profile(request):
    context = {'user': request.user}
    return render(request, 'profile.html', context)