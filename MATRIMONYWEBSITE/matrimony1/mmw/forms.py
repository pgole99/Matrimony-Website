from django import forms
from .models import personinfo
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class personform(forms.ModelForm):
    class Meta:
        model=personinfo
        fields=['name','email','gender','date','religion','city','age','physical_disability','education','occupation','img','biodata']
        labels={'name':' Full Name','email':'Email','img':'Image_Upload','biodata':'Biodata'}
        widgets={'name':forms.TextInput(attrs={'class':'form-control'}),
                 'email':forms.EmailInput(attrs={'class':'form-control'}),
                 'date':forms.DateInput(attrs={'class':'form-control','id':"datepicker"}),
                 'religion':forms.TextInput(attrs={'class':'form-control'}),
                 'city':forms.TextInput(attrs={'class':'form-control'}),
                 'age':forms.NumberInput(attrs={'class':'form-control'}),
                 'physical_disability':forms.TextInput(attrs={'class':'form-control'}),
                 'education':forms.TextInput(attrs={'class':'form-control'}),
                 'occupation':forms.TextInput(attrs={'class':'form-control'}),
                 }
        
class usersignup(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'email':'Email Add'}
    