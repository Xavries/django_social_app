from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Room, Topic
from .forms import Room_form
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

#rooms = [
#    {'id':1, 'name':'Learn django'},
#    {'id':2, 'name':'Learn 2django'},
#    {'id':3, 'name':'Learn 3django'}
#]

def login_page(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password is wrong')

    context = {'page':page}
    return render(request, 'base/login_register.html', context)

def logout_user(request):
    logout(request)
    return redirect('home')

def register_user(request):
    page = 'register'
    form = UserCreationForm(request.POST)

    if form.is_valid():
        user = form.save(commit=False)
        user.username = user.username.lower()
        user.save()
        login(request, user)
        return redirect('home')
    else:
        messages.error(request, 'An error ocurred during registration')

    context = {'page':page, 'form':form}
    return render(request, 'base/login_register.html', context)


def home(request):
    q = request.GET.get('q') if request.GET.get('q')!=None else ''
    # q is equal to whatever we pass to the url when using search

    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
        )
    # so what is this filter about:
    # Q gives us a possibility to make "and(&)" and "or(|)" statements
    # "topic__name__icontains" where topic is variable from class Room
    # "name" means topic name
    # "icontains" means that result contains text we type in search
    # "i" in icontains means that result contains text we type in search in ANY part of result
    
    topics = Topic.objects.all()
    room_count = rooms.count()

    context = {'rooms':rooms, 'topics':topics, 'room_count':room_count}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    
    context = {'room':room}

    return render(request, 'base/room.html', context)

@login_required(login_url='login')
def create_Room(request):
    form = Room_form()
    if request.method == 'POST':
        print(request.POST)
        form = Room_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
            
    context = {'form':form}
    return render(request, 'base/room_form.html', context)

@login_required(login_url='login')
def update_Room(request, pk):
    room = Room.objects.get(id=pk)
    form = Room_form(instance=room)

    if request.user != room.host:
        return HttpResponse('You are not allowed here')

    if request.method == 'POST':
        form = Room_form(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'base/room_form.html', context)

@login_required(login_url='login')
def delete_Room(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj':room})
