from django.db import models
from users.models import User
# Create your models here.
class CodeSnippet(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='code_snippet')
    title = models.CharField(max_length=255)

# class Title(models.Model):
#     user = models.ForeignKey(to=User, on_delete=models.CASCADE,
#     related_name='title')
#     title = models.CharField(max_length=255)
    
# class Description(models.Model):
#     user = models.ForeignKey(to=User, on_delete=models.CASCADE,
#     related_name='description')
#     language = models.CharField(max_length=255) 
#     date_of_creation = models.CharField(max_length=255)
#     tag_field = models.CharField(max_length=255)
    
# class Code(models.Model):
#     user = models.ForeignKey(to=User, on_delete=models.CASCADE,
#     related_name='body')
#     text = models.CharField(max_length=255)
