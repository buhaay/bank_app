from django import forms
from .models import User, TransferFunds
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class TransferFundsForm(forms.ModelForm):

    class Meta:
        model = TransferFunds
        fields = [
            'receiver',
            'total'
        ]
