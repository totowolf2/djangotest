from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    return render(request, 'index.html', {
        'test': 'FOOBAR',
        'food':['water','soda','apple']
    })