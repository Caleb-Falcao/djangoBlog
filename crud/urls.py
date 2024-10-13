from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Rota para a pagina inicial
    path('posts/', views.post_list, name='post_list'),  # Rota para a lista de postagens
    path('posts/new', views.post_create, name='post_create'),  # Rota para criar uma nova postagem
    path('posts/edit/<int:pk>/', views.post_edit, name='post_edit'),  # Rota para editar uma postagem existente
    path('posts/delete/<int:pk>/', views.post_delete, name='post_delete'),  # Rota para excluir uma postagem
]
