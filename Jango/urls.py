"""Jango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import include, path 
from code_snippet import views as code_snippet_views



urlpatterns = [
    path('', code_snippet_views.homepage, name="homepage"),
    path('code_snippet/', code_snippet_views.snippet_list, name='snippet_list'),
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    path('code_snippet/<int:snippet_pk>/', code_snippet_views.snippet_detail, name='snippet_detail'),
    path('code_snippet/add_new_snippet', code_snippet_views.add_new_snippet, name="add_new_snippet"),
    path('code_snippet/<int:snippet_pk>/edit_snippet/', code_snippet_views.edit_snippet, name='edit_snippet'),
    path('code_snippet/<int:snippet_pk>/delete_snippet/', code_snippet_views.delete_snippet, name='delete_snippet'), 
    path('code_snippet/search_snippet/', code_snippet_views.search_snippet, name='search_snippet'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
