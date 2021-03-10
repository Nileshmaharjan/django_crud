from django.db import models

class Monuments(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    coverImage = models.CharField(max_length=1000, blank=False, default='')
    description = models.CharField(max_length=2000, blank=False, default='')
    history = models.CharField(max_length=2000, blank=False, default='')
    
class LocalFood(models.Model): 
    title = models.CharField(max_length=70, blank=False, default='')
    coverImage = models.CharField(max_length=1000, blank=False, default='')
    description = models.CharField(max_length=2000, blank=False, default='')
    history = models.CharField(max_length=2000, blank=False, default='')