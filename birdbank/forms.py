from django import forms
from django.contrib.auth import authenticate


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user or not user.check_password(password):
                raise forms.ValidationError("Invalid User Credentials.")
        return super(UserLoginForm, self).clean(*args, **kwargs)
        '''
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("This user not exists")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect Password")
        return super(UserLoginForm, self).clean(*args, **kwargs)
        '''