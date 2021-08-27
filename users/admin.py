from django.contrib import admin
from .models import Profile

admin.site.register(Profile)


# classes registered for an app will show up on admin
# page as category (this is what we want)
# Do this after creating model, makemigrations, and finally migrate
 