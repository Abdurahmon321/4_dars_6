from django import forms
from .models import Car, Category, Color


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['category', 'make', "color", 'model', 'year', 'price', 'image']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class ColorForm(forms.ModelForm):
    class Meta:
        model = Color
        fields = ["color"]
