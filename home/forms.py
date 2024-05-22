from django import forms
from .models import Event


class createEventform(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'event_date']
        widgets = {
            'event_date': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }

class EditEventform(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'event_date']