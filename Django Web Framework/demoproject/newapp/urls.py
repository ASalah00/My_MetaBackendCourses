from django.urls import path,include
from . import views
app_name='newapp' 
urlpatterns = [
    #include the urls of the demoapp incase we got the demoapp/ path
    path('newindex/',views.index ,name='index'),
    path('fakelogin2/',views.fakelogin2 ,name='fakelogin2'),
    path('fakelogin3/',views.fakelogin3 ,name='fakelogin3'),
]
