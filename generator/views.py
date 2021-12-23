from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    # return HttpResponse("Hello There")
    return render(request, 'home.html')

def about(request):
    # return HttpResponse("Hello There")
    return render(request, 'about.html')
#
def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend( list('ABCDEFGHIJKLMNOPQRSTUVWXYZ') )
    if request.GET.get('numbers'):
        characters.extend( list('0123456789') )
    if request.GET.get('specials'):
        characters.extend( list('$@%^&') )

    length = int(request.GET.get('length',12))  #taking from user #default value is set
    thepassword = ''
    for i in range(length):
        thepassword += random.choice(characters)
    return render(request, 'password.html',{'password' : thepassword})

