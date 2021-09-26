from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

urlpatterns = [
    path('', PostListView.as_view(), name = 'blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name = 'user-posts'),
    path('about/', views.about, name = 'blog-about'),
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'post-detail'), #pk acts as a variable since multiple different posts could be called through it - what detailview expects
    path('post/new/', PostCreateView.as_view(), name = 'post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name = 'post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name = 'post-delete')
]

#Views.home is function from views.py that returns HTTP repsonse
#empty pattern that matched empty route from urls.py django (which is empty bc nothing after 'localhost:8000/blog')
#no empty pattern for the second path - now about/ is in there bc the address is for 'localhost:8000/blog/about'