from django.db import models

# Create your models here.

class person(models.Model):
    first_name = models.CharField(max_length=50,  default="Unknown")
    last_name = models.CharField(max_length=50, default="Unknown")
    password =  models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50, default="Unknown")

class minecrafe(models.Model):
    des = models.TextField()
    name = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    score = models.CharField(max_length=2)
    platform = models.CharField(max_length=50)

class spiderman(models.Model):
    des = models.TextField()
    name = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    score = models.CharField(max_length=2)
    platform = models.CharField(max_length=50)

class doom(models.Model):    
    des = models.TextField()
    name = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    score = models.CharField(max_length=2)
    platform = models.CharField(max_length=50)

class blackmyt(models.Model):
    des = models.TextField()
    name = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    score = models.CharField(max_length=2)
    platform = models.CharField(max_length=50)

class cyberpunk(models.Model):
    des = models.TextField()
    name = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    score = models.CharField(max_length=2)
    platform = models.CharField(max_length=50)