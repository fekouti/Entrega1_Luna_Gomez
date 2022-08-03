from django.shortcuts import render
from appUsers.models import *

# Create your views here.
def profile(request):
    return render(request, 'profile.html', context={})


def list_posts(request):
    posts = Posts.objects.all()
    print(len(posts))
    context = {
        'posts':posts
    }
    return render(request, 'profile.html', context=context)