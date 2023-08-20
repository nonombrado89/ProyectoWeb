from django.shortcuts import render
from blog.models import Post, Categoria

# Create your views here.
def blog(request):
    posts = Post.objects.all()
    return render(request, "blog/blog.html", {"posts": posts})

def categoria(request, categoria_id):

    categorias = Categoria.objects.get(id=categoria_id)
    posts = Post.objects.filter(categorias=categorias)
    return render(request, "blog/categoria.html", {"categoria": categoria, "posts": posts})