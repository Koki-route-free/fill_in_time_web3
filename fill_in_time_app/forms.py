from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import UserDB, ContentsDB

class UserCreateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #htmlの表示を変更可能にします
        self.fields['username'].widget.attrs['class']  = 'form-control'
        self.fields['email'].widget.attrs['class']     = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

    class Meta:
       model = UserDB
       fields = ("username", "email", "password1", "password2",)


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       #htmlの表示を変更可能にします
       self.fields['username'].widget.attrs['class'] = 'form-control'
       self.fields['password'].widget.attrs['class'] = 'form-control'


class ContentsCreateForm(forms.ModelForm):

    #htmlの表示を変更可能にします
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['address'].widget.attrs['class'] = 'form-control'
        self.fields['homepage'].widget.attrs['class'] = 'form-control'
        self.fields['classification'].widget.attrs['class'] = 'form-control'
        self.fields['telephone'].widget.attrs['class'] = 'form-control'
        self.fields['picture'].widget.attrs['class'] = 'form-control'
        self.fields['price'].widget.attrs['class'] = 'form-control'
        self.fields['detail'].widget.attrs['class'] = 'form-control'
        self.fields['open_time'].widget.attrs['class'] = 'form-control'
        self.fields['not_open_day'].widget.attrs['class'] = 'form-control'
        self.fields['min_stay_time'].widget.attrs['class'] = 'form-control'
        self.fields['max_stay_time'].widget.attrs['class'] = 'form-control'
        self.fields['how_come'].widget.attrs['class'] = 'form-control'
        self.fields['comments'].widget.attrs['class'] = 'form-control'
        self.fields['star'].widget.attrs['class'] = 'form-control'
        
    class Meta:
        model = ContentsDB
        fields = ("name", "address", "homepage", "classification", "telephone", "picture", "price", "detail", "open_time", "not_open_day", "min_stay_time", "max_stay_time", "how_come", "comments", "star")