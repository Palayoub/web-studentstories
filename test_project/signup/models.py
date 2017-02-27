from django.db import models

# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    age=models.IntegerField(default=15)
    date_bith=models.DateTimeField()

    print('Sign up now !')
    name = input('Your Name: ')
    email = input('Your Email: ')
    password = input('Your Password: ')




