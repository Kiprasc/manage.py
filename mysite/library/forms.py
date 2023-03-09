from .models import Profilis, QuoteInstance
from django import forms
from django.contrib.auth.models import User
from .models import *



class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class DateInput(forms.DateInput):
    input_type = 'date'

class UserQuoteInstanceCreateForm(forms.ModelForm):
    class Meta:
        model = QuoteInstance
        fields = ['email', 'reader', 'due_back', 'summary']
        widgets = {'reader': forms.HiddenInput(), "due_back": DateInput()}

