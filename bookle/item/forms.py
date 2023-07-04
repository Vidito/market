from django import forms

from .models import Item

INPUT_CLASSES = 'w-full py-3 px-5 bg-white rounded-md border'

class NewItemForm(forms.ModelForm):
    
    class Meta:
        
        model = Item            
        fields = ('category', 'name', 'description', 'price', 'image',)
        widgets = {
            'category': forms.Select(                
                attrs={
                'class': INPUT_CLASSES,            
            }
            ),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Item name'
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Write a description...'
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 0.00
            }),
            'image': forms.FileInput(attrs={
                'class': 'w-full bg-white p-3 rounded-md'})

        }

        

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image', 'is_sold')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }