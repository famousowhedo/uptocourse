from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Profile(models.Model):
    First_Name = models.CharField(max_length=30)
    Last_Name = models.CharField(max_length=30)
    Age = models.IntegerField()
    Nationality = models.CharField(max_length=30)
    Freelance = models.CharField(max_length=30, default='Available')
    Address = models.CharField(max_length=30)
    Phone = models.IntegerField()
    Email = models.CharField(max_length=30) 
    Facebook = models.CharField(max_length=30)
    Langages = models.CharField(max_length=30, default='English')   



class Post(models.Model):
    img = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=300)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    link_to_course = models.URLField()
    def __str__(self):
        return f'{self.author}'
    
    


class Contact(models.Model):
    your_name = models.CharField(max_length=30,default='YOUR NAME')
    you_email = models.EmailField(default= "YOUR EMAIL")
    your_message = models.TextField(default='YOUR MESSAGE')
    your_subject = models.CharField(max_length=30, default='YOUR SUBJECT')

    def __str__(self):
        return self.your_name
    

 
    