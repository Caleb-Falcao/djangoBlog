from django.db import models

# Create your models here.

# Classe que define o modelo 'Post', que representa uma postagem no blog.
class Post(models.Model):
    # Campo 'title', que armazena o título da postagem, com um limite máximo de 150 caracteres
    title = models.CharField(max_length=150)
    # Campo 'content', que armazena o texto da postagem, sem limite de tamanho
    content = models.TextField()
    # Campo 'created_at', que armazena a data e hora em que a postagem foi criada. Define automaticamente a data/hora atual quando a postagem é criada
    created_at = models.DateTimeField(auto_now_add=True)
    # Campo 'updated_at', que armazena a data e hora da última atualização da postagem. Atualiza automaticamente toda vez que a postagem é salva
    updated_at = models.DateTimeField(auto_now=True)