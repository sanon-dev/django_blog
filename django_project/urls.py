"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static 

# importing static as we are serving static files to client

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name = 'register'),
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name = 'logout'),
    path('profile/', user_views.profile, name = 'profile'),  
    # path('blog/', include('blog.urls')),  
    path('', include('blog.urls')), #Removing 'blog/' from pattern makes homepage 
                                    #go straight through localhost:8000 and not localhost:8000/blog
                                    # also this means that localhost:8000/blog/about is now just localhost:8000/about
                       
] 


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# Only adding this on when in debug mode


# auth_views.LoginView and auth_views.LogoutView are class specific views. 
# Handles logic but not the form/template

# Passing in 'template_name = ...', telling the program to look there for the HTML.
# This is a better way of doing these templates than creating templates folders in each app directory


