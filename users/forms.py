from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#This form created so that we can use it instead if usercreation form. Has the add-on 
# of asking for eail when an account is created 
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:         
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # fields are the fields we want in list in order
        #password2 is password confirmation - dev server wont work if named anything else