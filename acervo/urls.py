from django.urls import path
from .views import LivroListView, LivroDetailView, AutorListView, AutorDetailView

urlpatterns = [
    path('livros/', LivroListView.as_view(), name='livro_list'),
    path('livros/<int:pk>/', LivroDetailView.as_view(), name='livro_detail'),
    path('autores/', AutorListView.as_view(), name='autor_list'),
    path('autores/<int:pk>/', AutorDetailView.as_view(), name='autor_detail'),
]