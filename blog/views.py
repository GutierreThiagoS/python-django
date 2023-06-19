from django.shortcuts import render

from blog.data import posts

# Create your views here.

def blog(request):

    context = {
        'title': 'Blog',
        'posts': posts
    }

    return render(
        request, 
        'blog/home.html',
        context
    )

def post(request, id):

    context = {
        'title': 'Post',
        'posts': posts
    }

    return render(
        request, 
        'blog/home.html',
        context
    )



def exemplo(request):

    context = {
        'text': "Testando Exemplo",
        'title': 'Exemplo'
    }

    return render(
        request, 
        'blog/exemple.html',
        context
    )