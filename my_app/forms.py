from django import forms
from .models import Watering


class WateringForm(forms.ModelForm):
    class Meta:
        model = Watering
        fields = ["date"]
        widgets = {
            "date": forms.DateInput(
                format=("%Y-%m-%d"),
                attrs={"placeholder": "Select a date", "type": "date"},
            ),
        }
