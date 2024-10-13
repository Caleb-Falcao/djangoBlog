from django.contrib import admin
from .models import Post

# Register your models Post admin Django

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at') # Campos exibidos na lista de postagens
    search_fields = ('title','content') # Campos de busca

admin.site.register(Post, PostAdmin)

