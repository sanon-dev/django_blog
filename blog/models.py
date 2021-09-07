from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length = 100)      #characters field with max length rescription of 100
    content = models.TextField()
    #date_posted = models.DateTimeField(auto_now_add= True) #auto_now_add = True sets the time to when first posted, but cant ever update
    date_posted = models.DateTimeField(default = timezone.now)
    last_modified = models.DateTimeField(auto_now= True) #every time post is changed this will be set the time it was sent
    author = models.ForeignKey(User, on_delete=models.CASCADE) #if user is deleted, delete the post as well
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})
    #find location to specific post, searchong for the post detail page for whatever pk associated to the post

# Models are classes that contain data about an object/functionality. Django authomatically makes
# table in database based on model's information. 