from django.shortcuts import render
#from django.http import HttpResponse #No longer needed if using render

#following is dummy data that we use to pass into render func
posts = [
    {
        'author': 'AJ S',
        'title':'Blog Post 1',
        'content':'First post content',
        'date_posted':'August 14, 2021'
    },
    {
        'author': 'John Doe',
        'title':'Blog Post 2',
        'content':'Second post content',
        'date_posted':'August 15, 2021'
    }
]

#Return what we want user to see when they go to this route
#Handles traffic from home page of blog
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)    #render still returns Httpresponse
                                                        #context allows us to pass our data in to template and let us access it their within the template

#Handles traffic from about page of blog
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

