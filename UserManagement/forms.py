from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import datetime

from django.forms import TextInput


class Registration_Form(UserCreationForm):
    username = forms.RegexField(   label="Username", max_length=30, regex=r"^[\w.@+-]+$",
        help_text="Required. 30 characters or fewer. Letters, digits and "
                    "@/./+/-/_ only.",
        error_messages={
            'invalid': ("This value may contain only letters, numbers and "
                         "@/./+/-/_ characters.")},
        widget=TextInput(attrs={'class': 'form-control',
                                'required': 'true',
                                'placeholder': 'Enter your Username'
                                })
    )

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'required': 'true',
                                          'placeholder': 'Enter your password',


                                          })
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'type': 'password',
                                          'required': 'true',
                                          'placeholder': 'Enter your password again',
                                          }),
        help_text="Enter the same password as above, for verification."
    )

    email = forms.EmailField(
        label="Email",

        widget=forms.EmailInput(attrs={'class': 'form-control',
                                          'required': 'true',
                                          'placeholder': 'Enter your Email',
                                          }),
        help_text="Enter the same password as above, for verification."
    )

    last_name = forms.CharField(required = False ,label=  "Last name ",label_suffix="   *not required",widget=forms.TextInput(

        attrs=
        {
            'class': 'form-control',
             'placeholder': 'Enter your Last name',

        }))

    first_name = forms.CharField(required = False ,label=  "First name ",label_suffix="   *not required",widget=forms.TextInput(

        attrs=
        {
            'class': 'form-control',
             'placeholder': 'Enter your First name',

        }))



    birthday = forms.DateField(required = False, input_formats= ['%Y-%m-%d','%m/%d/%Y','%m/%d/%y'],  initial=datetime.date.today, widget=forms.DateInput(

        attrs=
        {
            'class': 'form-control',
            'required': 'False',
            'placeholder': 'RRRR/MM/DD',



        }))




    def save(self,commit = True):
        user = super(Registration_Form, self).save(commit = False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.birthday = self.cleaned_data['birthday']
        Registration_Form.password=self.cleaned_data['password1']
        user.set_password(Registration_Form.password)
        if commit:
            user.save()

        return user

class UserLoginForm(forms.Form):
    Username=forms.CharField(label="Username")
    password=forms.CharField(label="Password",widget=forms.PasswordInput)