from django.db import models

class CoreConfig(models.Model):
    class Meta:
        app_label = 'core'

class Student(CoreConfig):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    # Add more fields as needed

class Teacher(CoreConfig):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    # Add more fields as needed
