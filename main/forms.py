from django.forms import ModelForm, TextInput,NumberInput
from .models import man


# class BuilderForm(ModelForm):
#     class Meta:
#         model = Builder
#         fields = ['name', 'second_name']
#
#         widgets = {
#             "name": TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder' : 'Имя'
#             }),
#
#             "second_name": TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Фамилия'
#             }),
#
#
#
#         }