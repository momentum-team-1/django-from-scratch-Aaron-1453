from django.db import models
from users.models import User
from taggit.managers import TaggableManager
from django.db.models import Q
# Create your models here.




    
class CodeSnippet(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='code_snippets', null=True)
    title = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    body = models.TextField(max_length=2000)
    tags = TaggableManager()
    def __str__(self):
        return self.title

def search_snippet_for_user(user, query):
    return user.code_snippet.filter(Q(title__icontains=query))

    

    

