from django import forms
from .models import Tweet, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']
      
# class UserRegistrationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email','password1', 'password2']

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    photo = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'photo']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            profile = Profile(user=user, photo=self.cleaned_data['photo'])
            profile.save()
        return user
