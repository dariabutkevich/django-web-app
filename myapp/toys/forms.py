from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, Select, NumberInput, FileInput
from .models import Toy  # подключаем модель из models, а не admin

class ToyForm(ModelForm):
    class Meta:
        model = Toy
        fields = ['image', 'name', 'category', 'description', 'design', 'height', 'material']
        widgets = {
            "image": FileInput(attrs={
                'class': 'form-control',
            }),
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),
            "category": Select(attrs={
                'class': 'form-control'
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'
            }),
            "design": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дизайн / Автор'
            }),
            "height": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Высота'
            }),
            "material": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Материал'
            })
        }
