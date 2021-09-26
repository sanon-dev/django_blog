# django_blog

This blog was created as a summer programming to sharpen skills and take the time to learn a new tech stack. 

## Site Dependencies 

![dependencies](https://user-images.githubusercontent.com/47250909/134817838-0dc09129-65fe-4e22-b4ea-df073428edd7.PNG)

## Functionality

![diagram](https://user-images.githubusercontent.com/47250909/134819642-e0d11314-4f13-4488-8436-a45cd6e6c8a2.png)
*A photo of the home page of this blog side by side with the HTML template for page structure (top) and post layout (bottom)*

Django projects runs under a model-view-controller (MVC) framwork, with a URL launcher serving as the controller which users interact with by clicking through different sections of the site. This controller updates class-based models (written in Python), which then update the view seen by users with function-specific HTML/CSS. For this site, two internal applications made up the projects - users and blog. The former handles all user-related needs and the latter containing all info for the various different blog pages. 

Major class-based views within this project include:

- PostListView (within users/views.py)
```python
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted'] # reverse chronological order, check to see if inherits all this stuff from listview
    paginate_by = 4 # Sets num of posts per page
```

- UserPostListView (within users/views.py)
Nearly identical to PostListView with an additional function to filter out posts to just those written by the user.
```python
def get_queryset(self):   #Overriden function
  user = get_object_or_404(User, username=self.kwargs.get('username'))
  return Post.objects.filter(author = user).order_by('-date_posted')
```

- profile (within blog/views.py)
```python
@login_required     # <- that is known as a decorator - allows user to add functionality to an object
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance = request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
        # Instances in the form parameters used to populate the respective fields
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your account has been updated.')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance = request.user)
        profile_form = ProfileUpdateForm(instance = request.user.profile)
            

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(request, 'users/profile.html', context)
```
