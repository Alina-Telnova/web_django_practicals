from django import forms
from .models import Organization, Position, UsersOrganizations
from django.contrib.auth.models import User

class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['organization_name', 'founding_date', 'address', 'director_name']

class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = ['name']

class UsersOrganizationsForm(forms.ModelForm):
    class Meta:
        model = UsersOrganizations
        fields = ['user', 'organization', 'position', 'hire_date', 'dismissal_date']
        widgets = {
            'hire_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'dismissal_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }