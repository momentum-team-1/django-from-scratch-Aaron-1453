from django.shortcuts import render, redirect
from users.models import User
from .models import CodeSnippet
# Create your views here.
def homepage(request):
    return render(request, "code_snippet/home.html")

def snippet_list(request):
    code_snippet = request.user.snippet_list.all()
    return render(request, "code_snippet/snippet_list.html", {"code_snippet": code_snippet})