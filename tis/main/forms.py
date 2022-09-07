from logging import PlaceHolder
from tkinter import Widget
from django import forms
from .models import *


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer

        fields = ['answer_1', 'answer_2', 'answer_3', 'answer_4', 'answer_5',
                  'answer_6', 'answer_7', 'answer_8', 'answer_9', 'answer_10']

        widgets = {
            'answer_1': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '2,5'}),
            'answer_2': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '2,5'}),
            'answer_3': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '2,5'}),
            'answer_4': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '2,5'}),
            'answer_5': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '2,5'}),
            'answer_6': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '2,5'}),
            'answer_7': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '2,5'}),
            'answer_8': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '2,5'}),
            'answer_9': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '2,5'}),
            'answer_10': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '2,5'})}


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['name', 'surname', 'patronymic', 'school',
                  'mail', 'number', 'letter', 'certificate']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Иван'
            }),
            'surname': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Иванов'
            }),
            'patronymic': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Иванович'
            }),
            'mail': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'you@example.com'
            }),
            'school': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'МБОУ Приволжская СОШ №1'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'Placeholder': 'Придумайте пароль'
            })
        }
