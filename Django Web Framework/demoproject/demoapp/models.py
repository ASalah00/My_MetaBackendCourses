from django.db import models

# Create your models here.
class Person(models.Model): 
    person_name = models.CharField(max_length=20) 
    email = models.EmailField() 
    phone = models.CharField(max_length=20) 
    age=models.IntegerField(default=0)
    def __str__(self): 
        return f"{self.person_name}" 

class MenuCategory(models.Model):
    #id PK is made by default
    category_name=models.CharField(max_length=200)
    def __str__(self):
        return self.category_name

class Menu(models.Model):
    menu_item=models.CharField(max_length=200)
    price=models.IntegerField(null=False)
    #the category id that the menu item belongs to it is FK
    #FK TAKES THE TABLE YOU WANT TO LINK TO AND SETTINGS
    category_id=models.ForeignKey(MenuCategory,on_delete=models.PROTECT,default=None)
    def __str__(self):
        return self.menu_item


class Logger(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200) 
    time_log=models.TimeField(help_text='Enter the exact time')           