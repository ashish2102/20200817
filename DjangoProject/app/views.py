from django.shortcuts import render
from django.http import HttpResponse
import operator

def home(requests):
    return render(requests,'app/home.html')

def aboutus(requests):
    return render(requests,'app/about.html',{'userid':'ashishuserid'})

    
