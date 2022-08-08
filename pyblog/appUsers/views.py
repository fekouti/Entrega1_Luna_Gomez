from django.shortcuts import render, redirect
from appUsers.models import *
from django.http import HttpResponse

# Create your views here.
def profile(request):
    return render(request, 'profile_posts/profile.html', context={})
    
def allUsers(request):
    return render(request, 'users/all_users.html', context={})

def reviews(request):
    return render(request, 'reviews/reviews.html', context={})


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


def new_review(request):
    print("hola")
    if request.method == 'POST':
        print("esto")
        name= request.POST['name']
        print("es")
        stars= request.POST['stars']
        print("una")
        detailedReview= request.POST['detailedReview']
        print("prueba")
        
        new_review = Reviews(name=name, stars=stars, detailedReview=detailedReview)
        print("de")
        new_review.save()
        print("funcionamiento")
    return render(request, 'reviews/new_review.html', context={})



# Definir la vista de la clase




# Definir la funcion que toma los datos del form


def searchPosts(request):
    return render(request, "profile_posts/search_post.html",context={})


def search(request):
    if request.method == 'GET':
        print("hola")
        if request.GET['Search']:
            print("hola")
            post = request.GET['Search']
            posts = Posts.objects.filter(title__icontains=post)
            print("hola")
            return render(request, "profile_posts/search_post.html", {"posts":posts , "post":post})

        else:

            response = "No se encontraron resultados"
            print("hola")
    else:
        print("esto no se esta ejecutando")
    return HttpResponse(response)