from django import forms
from .models import information


class Infopost(forms.ModelForm):
    class Meta:
        model = information()
        fields = ["fname", "lname", "phone", "company","email"]