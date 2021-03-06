from django import forms
from .models import Patient


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        exclude = ()
        widgets = {
            'id': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'min': 1,
                    'type': 'number',
                }
            ),
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'birth_date': forms.DateInput(
                attrs={
                    'placeholder': 'dd/mm/aaaa',
                    'class': 'form-control',
                }
            ),
            'collection_date': forms.DateInput(
                attrs={
                    'placeholder': 'dd/mm/aaaa',
                    'class': 'form-control',
                }
            ),
            'delivery_date': forms.DateInput(
                attrs={
                    'placeholder': 'dd/mm/aaaa',
                    'class': 'form-control',
                }
            ),
            'doctor_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
        }
