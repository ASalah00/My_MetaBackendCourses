from django.urls import path 
from . import views 
app_name='demoapp' 
urlpatterns = [ 
    #path function takes as argument ('routname',the view function you will call)
    path('', views.index, name='index'), 
    path('test/', views.test, name='test'), 
    path('paramview/<name>/<int:id>', views.paramview, name='paramview'), 
    path('queryview/', views.queryview, name='queryview'), 
    path('showform/', views.showform, name='showform'), 
    path('processform/', views.processform, name='processform'), 
    path('form_logger/', views.form_logger, name='form_logger'), 
    path('myspeciallogin/', views.login, name='login3'), 
    path('about/', views.about, name='about'), 
    path('menubyid/', views.menu_by_id, name='menubyid'), 
    path('home/', views.home, name='home'), 
    path('register/', views.register, name='register'), 
    path('login/', views.login, name='login'), 
] 