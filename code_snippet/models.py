from django.db import models
from users.models import User
# Create your models here.

class Tag(models.Model):
    tag = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.tag
    
class CodeSnippet(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='code_snippets', null=True)
    title = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    created_at = models.DateField(max_length=255)
    body = models.CharField(max_length=2000)
    tags = models.ManyToManyField(to=Tag, related_name='code_snippets')
    
    def __str__(self):
        return self.title


    
    

    

