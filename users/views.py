from django.shortcuts import render, redirect # redirect added manually
# from django.contrib.auth.forms import UserCreationForm # creates user with no priviges from given user and pass # replaced with userregistartion form
from django.contrib import messages # Imported to use to create pop up messgae that acct created 
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required # Importing a decorator to make sure only logged in users can see profile page

def register(request):
    if request.method == 'POST':                # checking if method is same as form method in users/register.html
        form = UserRegisterForm(request.POST)   # if so, create a form to fill out using POST info
        if form .is_valid():                    # check that form is created and send out pop up to infrom user   
            form.save()                         # actually saves info we entered and creates user
            username = form.cleaned_data.get('username')        
            messages.success(request, f'Account created for {username} ! You are now able to login')  # Pop message to show that user was created using f string
            return redirect('login') # returns us to login, the name of the url pattern for login page
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
    
@login_required     # <- that is known as a decorator - allows user to add functionality to an object
def profile(request):
    return render(request, 'users/profile.html')