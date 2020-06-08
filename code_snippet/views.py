from django.shortcuts import render, redirect, get_object_or_404
from users.models import User
from .models import CodeSnippet
from django.contrib.auth.decorators import login_required
# Create your views here.
def homepage(request):
    if request.user.is_authenticated:
        return redirect(to='snippet_list')
    return render(request, "code_snippet/home.html")

@login_required
def snippet_list(request):
    your_snippets = request.user.code_snippets.all()
    return render(request, "code_snippet/snippet_list.html", {"your_snippets": your_snippets})

@login_required
def snippet_detail(request, pk):
    snippet = get_object_or_404(request.user.code_snippets, pk=pk)
    return render(request, "code_snippet/snippet_detail.html", {"snippet": snippet})