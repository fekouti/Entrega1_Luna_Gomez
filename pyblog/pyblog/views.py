from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render


def inicio(request):
    return render(request, 'baseTemplate.html', context={})