from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)  # Creates reverse relational link with user
                                                                  #  ie creates key tied to this one user and allows items of the user's to be marked
                                                                  # second parameter deletes things related to user if user deleted
    image = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics')  # profile_pics is a directory
    
    bio = models.TextField(blank = 'true', default = 'My profile')

    def __str__(self):
        return f'{self.user.username} Profile'


    # Overriding default save to add functionality
    def save(self):
        
        super().save() # original save
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300: #Check if image is over 300px
            output_size = (300,300)
            img.thumbnail(output_size)  #Resize img and save
            img.save(self.image.path)

# Models are classes that contain data about an object/functionality. Django authomatically makes
# table in database based on model's information. 
