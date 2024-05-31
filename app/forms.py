from typing import Any
from django import forms
from app.models import *
from app.views import *
from django.core import validators

class TopicForm(forms.ModelForm):
     mobileno=forms.CharField(min_length=10,max_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])
     
     
     class Meta:
        model=Topic
        fields="__all__"


class WebpageForm(forms.ModelForm):
    reemail=forms.CharField()
    class Meta():
        model=Webpage
        fields="__all__"
    
    
    

    def clean(self):
        email=self.cleaned_data['email']
        reemail=self.cleaned_data['reemail']
        if email!=reemail:
            raise forms.ValidationError('check the email please ') 

    
    

        
    

        

    