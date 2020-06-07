from django.contrib import admin
from .models import Tag, CodeSnippet

# Register your models here.
admin.site.register(Tag)
admin.site.register(CodeSnippet)