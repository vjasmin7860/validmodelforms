from django.db import models

# Create your models here.
from django import forms
from django.core import validators 


def validators_for_a(value):
    if value[0]=='a':
        raise forms.ValidationError('should not start with a')
    
def validators_for_len(value):
    if len(value)<5:
        raise forms.ValidationError('length should not end lessthan 5')
#create your models here
class Topic(models.Model):
    topic_name=models.CharField(max_length=10,primary_key=True,validators=[validators_for_a,validators_for_len])
   
    def __str__(self):
        return self.topic_name
    
class Webpage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=10)
    url=models.URLField()
    email=models.EmailField()
    
    def __str__(self):
        return self.name
class AccessRecord(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date=models.DateField()
    author=models.CharField(max_length=10)

    def __str__(self):
        return self.name