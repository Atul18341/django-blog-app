from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

gender_options=(("1","None"),("2","Male"),("3","Female"),("4","Others"))

class NewUserForm(UserCreationForm):
   name=forms.CharField(required=True)
   email=forms.EmailField(required=True)
   age=forms.CharField(required=True)
   gender=forms.ChoiceField(choices=gender_options)
   class Meta:
     model=User
     fields=("name","username","email","password1","password2","age","gender")

   def save(self, commit=True):
       user=super(NewUserForm, self).save(commit=False)
       user.name=self.cleaned_data['name']
       user.email=self.cleaned_data['email']
       user.age=self.cleaned_data['age']
       user.gender=self.cleaned_data['gender']
       if commit:
         user.save()
       return user
