from django import forms
from ProjectTwo.models import User

class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ()
        # fields= '__all__'