from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render


def inicio(request):
    return render(request, 'index.html', context={})

def about(request):
    return render(request, 'about.html', context={})

def faq(request):
    return render(request, 'faq.html', context={})


def register(request):
    return render(request, 'register.html', context={})