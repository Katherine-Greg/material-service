from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Order, Customer


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = UserCreationForm.Meta.model
        fields = "__all__"
        field_classes = UserCreationForm.Meta.field_classes
        

class RequestForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["title", "items"]
        widgets = {
            "items": forms.SelectMultiple(attrs={"class": "select2"}),
            "created_for": forms.SelectMultiple(attrs={"class": "select2"}),
        }
