from django.shortcuts import render, redirect
from users.models import User
from .models import CodeSnippet
# Create your views here.
def homepage(request):
    if request.user.is_authenticated:
        return redirect(to='snippet_list')
    return render(request, "code_snippet/home.html")

def snippet_list(request):
    code_snippet = request.user.code_snippet.all()
    return render(request, "code_snippet/snippet_list.html", {"code_snippet": code_snippet})