from django.shortcuts import render
from django.http import HttpResponse
from django .template import loader 

from .models import Bd


def info (request):
    bbs = Bd.objects.all()
    return render(request, 'board/index.html', {'bbs': bbs}) 
