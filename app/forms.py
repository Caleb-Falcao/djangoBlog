from django import forms
from .models import Post

# Classe que define o formulário 'PostForm' baseado no modelo 'Post'.
class PostForm(forms.ModelForm):
    class Meta:
        # Especifica que este formulário usa o modelo 'Post'.
        model = Post
        # Define os campos do modelo 'Post' que serão incluídos no formulário.
        fields = ['title', 'content']

