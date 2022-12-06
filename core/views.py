from django.contrib import messages
from django.contrib.auth import authenticate, login as loginUser, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.template import context

from core.forms import TodoForm
from core.models import Todo


# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            loginUser(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Account not found.')
            return redirect('login')
    return render(request, 'login.html')


def signup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {
        'form': form

    }
    return render(request, 'register.html', context)


def signout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        user = request.user
        form = TodoForm()
        todo = Todo.objects.filter(user=user).order_by('-date')
    return render(request, 'view_page.html', {'form': form, 'todo': todo})


def search(request):
    if request.user.is_authenticated:
        user = request.user
        cat = request.POST['search-area']
        form = Todo.objects.filter(user=user, title__contains=cat)
    return render(request, "view_page.html", {'todo': form})


@login_required(login_url='login')
def add_todo(request):
    if request.user.is_authenticated:
        user = request.user
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = user
            todo.status = 'pending'
            todo.save()
            return redirect('home')
        else:
            return render(request, 'adding.html', {'form': form})


@login_required(login_url='login')
def delete_list(request, id):
    Todo.objects.get(id=id).delete()
    return redirect('home')


@login_required(login_url='login')
def update_task(request, pk):
    task = Todo.objects.get(id=pk)
    form = TodoForm(instance=task)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('home')
    context = {'form': form}
    return render(request, 'edit.html', context)
