# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()
    def __unicode__(self):
    # 在Python3中使用 def __str__(self):
        return self.name
    class Admin:
        pass
class Author(models.Model):
    salutation = models.CharField(max_length=10)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    headshot = models.ImageField(upload_to='tmp')
	
class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()
    
class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
     
    def __unicode__(self):
    # 在Python3中使用 def __str__(self):
        #return "name : %s,age : %s" % (self.name,self.age)
		return self.name