from django import forms

from .models import ConversationMessage

class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={
                'placeholder': 'Type your message here',
                'class': 'w-full mt-3 py-2 px-4 rounded-md border'
            }),
        }
        labels = {
        "content":  "",
    }
        
