from django import forms
from django.contrib.auth.models import User
from journal_app.models import Entry

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class NewEntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['title', 'content']
