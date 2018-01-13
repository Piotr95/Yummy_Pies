from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

import datetime

from django.forms import TextInput

from Ingredients.models import Ingredients


class  IngredientForm(forms.ModelForm):
    class Meta:
        model =Ingredients
        fields=['name', 'pics']


    name = forms.RegexField(   label="name", max_length=50, regex=r"^[A-Z][a-z]+$",
        help_text="Required. 50 characters or fewer. Letters",
        error_messages={
            'invalid': ("This value may contain only letters")},
        widget=TextInput(attrs={'class': 'form-control',
                                'required': 'true',
                                'placeholder': 'Enter ingredient name'
                                })
    )
    pics= forms.ImageField(label="Image",required=False, widget=forms.FileInput ,error_messages ={
        'invalid':'Image files only'})