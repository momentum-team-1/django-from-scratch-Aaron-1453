from django.shortcuts import render, redirect, get_object_or_404
from users.models import User
from .models import CodeSnippet, search_snippet_for_user
from django.contrib.auth.decorators import login_required
from .forms import SnippetForm
from django.db.models import Q
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
def snippet_detail(request, snippet_pk):
    snippet = get_object_or_404(request.user.code_snippets, pk=snippet_pk)
    return render(request, "code_snippet/snippet_detail.html", {"snippet": snippet})

@login_required
def add_new_snippet(request):
    if request.method == "POST":
        form = SnippetForm(data=request.POST)
        if form.is_valid():
            new_snippet = form.save(commit=False)
            new_snippet.user = request.user
            new_snippet.save()
            form.save_m2m()
        return redirect(to='snippet_detail', snippet_pk=new_snippet.pk)
    else:
        form = SnippetForm()
    return render(request, 'code_snippet/add_new_snippet.html', {"form": form})

@login_required
def edit_snippet(request, snippet_pk):
    snippet = get_object_or_404(request.user.code_snippets, pk=snippet_pk)
    
    if request.method == "POST":
        form = SnippetForm(instance=snippet, data=request.POST)
        if form.is_valid():
            snippet = form.save()
            return redirect(to='snippet_detail', snippet_pk=snippet.pk)

    else:
        form = SnippetForm(instance=snippet)
    
    return render(request, "code_snippet/edit_snippet.html", {'form': form, 'snippet': snippet})
    
@login_required
def delete_snippet(request, snippet_pk):
    snippet = get_object_or_404(request.user.code_snippets, pk=snippet_pk)
    if request.method == "POST":
        snippet.delete()
        return redirect(to="snippet_list")
    
    return render(request, "code_snippet/delete_snippet.html", {"snippet": snippet })

@login_required
def search_snippet(request):
    
    query = request.GET.get('q')

    if query is not None:
        snippet = CodeSnippet.objects.filter(Q(title__icontains=query))
    else:
        snippet = None

    return render(request, "code_snippet/search_snippet.html", {
        "snippet": snippet, 
        "query": query
    })
    
