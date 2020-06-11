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
        
