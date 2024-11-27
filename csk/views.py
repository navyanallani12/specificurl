from django.shortcuts import render

from django.http import HttpResponse
def captain(request):
    return HttpResponse('<h1>ruturaj is a captain of csk</h1>')
def vicecaptain(request):
    return HttpResponse('<h1> jd is vicecaptain</h1>')
