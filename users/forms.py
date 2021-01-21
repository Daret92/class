from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    def __init__(self,*args,**kwargs):
        super(SignUpForm,self).__init__(*args,**kwargs)
        for item in self.fields:
            self.fields[item].widget.attrs['class'] = 'form-control'
    class Meta:
        model = User
        fields = ['username','email','password1','password2','first_name','last_name']

class UpdateUpForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(UpdateUpForm, self).__init__(*args, **kwargs)
        for item in self.fields:
            self.fields[item].widget.attrs['class'] = 'form-control'
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']

class PasswordForm(forms.Form):
    contraseña_actual = forms.CharField(max_length=32,required=True,
                       widget= forms.TextInput
                       (attrs={'type':'password','class':'form-control form-control-lg'}))
    contraseña_nueva = forms.CharField(max_length=32,required=True,
                       widget= forms.TextInput
                       (attrs={'type':'password','class':'form-control form-control-lg'}))
    confirma_la_contraseña = forms.CharField(max_length=32,required=True,
                       widget= forms.TextInput
                       (attrs={'type':'password','class':'form-control form-control-lg'}))
