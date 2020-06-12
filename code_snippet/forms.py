from django import forms
from .models import CodeSnippet

class SnippetForm(forms.ModelForm):
    class Meta:
        model = CodeSnippet
        fields = [
            'title', 
            'language',  
            'body',
            'tags'
        ]
        
        widgets = {
        'title' : forms.TextInput(attrs={'class': 'pa1 w-50'}),
        'body': forms.TextInput(attrs={'class': 'pa5 w-50'}),
        'tags': forms.TextInput(attrs={'class': 'pa2 w-20'})
    }
