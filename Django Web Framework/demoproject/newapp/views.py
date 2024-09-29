from django.shortcuts import render
from django.http import HttpResponse,HttpResponsePermanentRedirect
from django.urls import reverse 
from django.shortcuts import redirect
# Create your views here.
def index(request):
    return HttpResponse("this is new index!")

def fakelogin2(request):
    #when the function executes the line below will redirect to the path in the demoapp that has name login
    return redirect(reverse('demoapp:login'))


def fakelogin3(request):
    #when the function executes the line below will redirect to the path in the demoapp that has name login
    return redirect(reverse('demoapp:login3'))