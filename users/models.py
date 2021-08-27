from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)  # Creates reverse relational link with user
                                                                  #  ie creates key tied to this one user and allows items of the user's to be marked
                                                                  # second parameter deletes things related to user if user deleted
    image = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics')  # profile_pics is a directory
    
    bio = models.TextField(blank = 'true', default = 'My profile')

    def __str__(self):
        return f'{self.user.username} Profile'

# Models are classes that contain data about an object/functionality. Django authomatically makes
# table in database based on model's information. 
