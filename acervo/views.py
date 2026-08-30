from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Livro, Autor

# Create your views here.
class LivroListView(ListView):
    model = Livro
    template_name = 'acervo/livro_list.html'
    context_object_name = 'livros'

class LivroDetailView(DetailView):
    model = Livro
    template_name = 'acervo/livro_detail.html'
    context_object_name = 'livro'

class AutorListView(ListView):
    model = Autor
    template_name = 'acervo/autor_list.html'
    context_object_name = 'autores'

class AutorDetailView(DetailView):
    model = Autor
    template_name = 'acervo/autor_detail.html'
    context_object_name = 'autor'