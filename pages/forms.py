from django import forms
from pages.models import UserModel

class UserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = '__all__'