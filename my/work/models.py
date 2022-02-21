from django.db import models
from django.contrib import admin

# Create your models here.
class Post(models.Model):
	title =models.CharField(max_length=100)
	desc =models.TextField(max_length=500)
