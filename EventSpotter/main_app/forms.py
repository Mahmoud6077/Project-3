from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser


class UserCreationForm(UserCreationForm):
    phone = forms.IntegerField(required=True, label='phone')
    email = forms.EmailField(max_length=100)

    class Meta:
        model = CustomUser
        fields = ("username", "phone","email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.phone = self.cleaned_data["phone"]
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user