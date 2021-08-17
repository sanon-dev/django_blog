from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length = 100)      #characters field with max length rescription of 100
    content = models.TextField()
    #date_posted = models.DateTimeField(auto_now_add= True) #auto_now_add = True sets the time to when first posted, but cant ever update
    date_posted = models.DateTimeField(default = timezone.now)
    last_modified = models.DateTimeField(auto_now= True) #every time post is changed this will be set the time it was sent
    author = models.ForeignKey(User, on_delete=models.CASCADE) #if user is deleted, delete the post as well

    def __str__(self):
        return self.title