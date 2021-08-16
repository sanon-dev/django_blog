from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'blog-home'),
    path('about/', views.about, name = 'blog-about'),
]

#Views.home is function from views.py that returns HTTP repsonse
#empty pattern that matched empty route from urls.py django (which is empty bc nothing after 'localhost:8000/blog')
#no empty pattern for the second path - now about/ is in there bc the address is for 'localhost:8000/blog/about'