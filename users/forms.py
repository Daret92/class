from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

Usuario = get_user_model()

class SignUpForm(UserCreationForm):
    def __init__(self,*args,**kwargs):
        super(SignUpForm,self).__init__(*args,*kwargs)
        for item in self.fields:
            self.fields[item].widget.attrs['class'] = 'form-control'
    class Meta:
        model = User
        fields = ['username','email','password1','password2','first_name','last_name']

#class UpdateUpForm(forms.ModelForm):
#    def __init__(self,*args,**kwargs):
#        super(SignUpForm,self).__init__(*args,*kwargs)
#        for item in self.fields:
#            self.fields[item].widget.attrs['class'] = 'form-control'
#    class Meta:
#        model = Usuario
#        fields = ['username','email','password1','password2','first_name','last_name']