from pyexpat import model
from django import forms
from index.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"