from django.shortcuts import render, redirect
from appUsers.models import *

# Create your views here.
def profile(request):
    return render(request, 'profile_posts/profile.html', context={})
    
def allUsers(request):
    return render(request, 'users/all_users.html', context={})


def list_posts(request):
    posts = Posts.objects.all()
    print(len(posts))
    context = {
        'posts':posts
    }
    return render(request, 'profile_posts/profile.html', context=context)

def list_users(request):
    users = Users.objects.all()
    print(len(users))
    context = {
        'users':users
    }
    return render(request, 'users/all_users.html', context=context)


def new_post(request):
    print("hola")
    if request.method == 'POST':
        print("esto")
        title= request.POST['title']
        print("es")
        subtitle= request.POST['subtitle']
        print("una")
        postContent= request.POST['content']
        print("prueba")
        
        new_post = Posts(title=title, subtitle=subtitle, postContent=postContent)
        print("de")
        new_post.save()
        print("funcionamiento")
    return render(request, 'profile_posts/new_post.html', context={})


def register(request):
    print("hola")
    if request.method == 'POST':
        print("esto")
        name= request.POST['name']
        print("es") 
        email= request.POST['email']
        print("una")
        password= request.POST['password']
        print("prueba")
        user = Users(name=name, email=email, password=password)
        print("de")


        user.save()
        print("funcionamiento")
    return render(request, 'users/register.html', context={})



# Definir la vista de la clase


# Definir la funcion que toma los datos del form