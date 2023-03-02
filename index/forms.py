from django import forms
from .models import *


class RegForm(forms.Form):
    PROGRAMS = [
        ('phy9', 'Физика 9'),
        ('phy11', 'Физика 11'),
        ('math1011', 'Математика 10-11')
    ]
    name = forms.CharField(max_length=40,
                           required=True,
                           label='Имя',
                           widget=forms.TextInput(attrs={'placeholder': 'Имя'}))
    phone = forms.IntegerField(required=True,
                               label='Телефон',
                               widget=forms.TextInput(attrs={'placeholder': 'Телефон'}))
    email = forms.EmailField(max_length=255,
                             required=True,
                             label='Email',
                             widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    programs = forms.CharField(label="Предмет",
                               widget=forms.Select(choices=PROGRAMS))
