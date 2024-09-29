from django.contrib import admin
from .models import Menu,MenuCategory,Logger,Person
from django.contrib.auth.models import User 
# Register your models here.
#you created a Model called Drink. 
# For this model to be editable in the admin interface, you must register it with the admin inside the admin.py file.
#e.gfrom .models import Drinks
#e.g admin.site.register(Drinks)
admin.site.register(Person)
admin.site.register(MenuCategory)
admin.site.register(Menu)
admin.site.register(Logger)
# Unregister the provided model admin:  
admin.site.unregister(User) 
from django.contrib.auth.admin import UserAdmin 
@admin.register(User) 
class NewAdmin(UserAdmin): 
    readonly_fields = [ 
        'date_joined', 
    ] 