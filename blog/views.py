from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin # similar to a decorator, makes sure that one is logged in, used for create post
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
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


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted'] # reverse chronological order, check to see if inherits all this stuff from listview

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user # Sets post author to currently logged in user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    success_url = '/'       # redirects back to whatever it is set to, in this case the homepage

    def form_valid(self, form):
        form.instance.author = self.request.user # Sets post author to currently logged in user
        return super().form_valid(form)

    def test_func(self):                # this func + user passes mixin, prevents user from modifying a post that they didn't initially make
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):                # this func + user passes mixin, prevents user from modifying a post that they didn't initially make
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



