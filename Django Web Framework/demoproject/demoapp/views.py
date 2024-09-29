from django.shortcuts import render
from django.http import HttpResponse
from .forms import ApplicationForm ,LogForm
from .models import Menu,MenuCategory
# Create your views here.

#In Django, a view is a function designed to handle a web request and return a web response.
# Each view function takes an HTTP Request object as its first parameter.
#after creating the view function we need to map it to url(routing) using urls.py (create it in the app package)
#and using path function you can map a routename to a view function
def index(request):
    return HttpResponse('Hello, world. This is the index view of Demoapp.')

def test(request): 
    path = request.path 
    method = request.method 
#     content=''' 
# <center><h2>Testing Django Request Response Objects</h2> 
# <p>Request path : " {}</p> 
# <p>Request Method :{}</p></center> 
# '''.format(path, method) 
    content = f"""
            <p>Request path : " {path}</p> 
            <p>Request Method :{method}</p></center> 
            """
    return HttpResponse(content) 

def paramview(request,name,id):
    return HttpResponse(f"""WELCOME TO PARAMVIEW YOUR NAME IS :{name} AND YOUR ID IS {id*5} """)#id is int so i can do math on it

def queryview(request):
    name=request.GET["name"]
    id=request.GET["id"]
    return HttpResponse(f"""WELCOME TO QUERYVIEW YOUR NAME IS :{name} AND YOUR ID IS {id} """)

def showform(request): 
    form=ApplicationForm()
    return render(request, "form.html",{'form': form}) 
def processform(request): 
    if request.method == "POST":
        form=ApplicationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name'] 
            add = form.cleaned_data['address'] 
            field = form.cleaned_data['field'] 
            return HttpResponse(f"""FORM SUBMITTED! THE DATA YOU ENTERED: name: {name} , address: {add} , field: {field}""")
    # if request.method == "POST": 
    #     id=request.POST['id'] 
    #     name=request.POST['name'] 
    # return HttpResponse("Name:{} UserID:{}".format(name, id)) 

def login(request):
    return HttpResponse("this is the real login page")

def form_logger(request):
    form=LogForm()
    if request.method=='POST':
        form=LogForm(request.POST)
        if form.is_valid():
            form.save()
    context={"form":form}
    return render(request,"logger_form.html",context)

def about(request):
    page_content={'name':'ahmedeka','age':'23'}
    return render(request,'about.html',{'content':page_content})

def menu_by_id(request):
    newmenu=Menu.objects.all()
    newmenu_dict={'menu':newmenu}
    return render(request,'menu.html',newmenu_dict)
def home(request): 
    return render(request, "home.html", {}) 

def register(request): 
    return render(request, "register.html", {}) 

def login(request): 
    return render(request, "login.html", {}) 