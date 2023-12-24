from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Order, Customer, Item


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = UserCreationForm.Meta.model
        fields = "__all__"
        field_classes = UserCreationForm.Meta.field_classes


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["title", "items", "created_for"]
        widgets = {
            "items": forms.SelectMultiple(attrs={"class": "select2"}),
            "created_for": forms.SelectMultiple(attrs={"class": "select2"}),
        }

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['items'].queryset = Item.objects.all()
        self.fields['created_for'].queryset = Customer.objects.all()
