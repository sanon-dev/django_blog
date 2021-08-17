from django.shortcuts import render
from .models import Post #. infront of models means from models file in current package
#from django.http import HttpResponse #No longer needed if using render


#Return what we want user to see when they go to this route
#Handles traffic from home page of blog
def home(request):
    context = {
        'posts': Post.objects.all() #collecting all the post info from its class
    }
    return render(request, 'blog/home.html', context)    #render still returns Httpresponse
                                                        #context allows us to pass our data in to template and let us access it their within the template

#Handles traffic from about page of blog
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

