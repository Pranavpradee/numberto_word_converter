from django import forms
from django.forms import ModelForm
from owner.models import owner



class NumtostringForm(ModelForm):
    class Meta:
        model=owner
        fields=["Number","Result"]
        widgets={
            "Number": forms.NumberInput(attrs={"class": "form-control"}),

            "Result":forms.TextInput(attrs={"class":"form-control"}),


        }