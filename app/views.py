from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm

# Página inicial do app
def index(request):
    return render(request, 'app/index.html')

# View para listar todas as postagens
def post_list(request):
    posts = Post.objects.all()  # Recupera todas as postagens do banco de dados
    return render(request, 'app/post_list.html', {'posts': posts})  # Renderiza a página com a lista de postagens

# View para criar uma nova postagem
def post_create(request):
    if request.method == 'POST':  # Verifica se o método da requisição é POST
        form = PostForm(request.POST)  # Cria um formulário com os dados enviados
        if form.is_valid():  # Verifica se o formulário é válido
            form.save()  # Salva a nova postagem no banco de dados
            return redirect('post_list')  # Redireciona para a página com a lista de postagens
    else:  # Se o método da requisição não for POST
        form = PostForm()  # Cria um formulário vazio
    return render(request, 'app/post_form.html', {'form': form})  # Renderiza a página com o formulário

# View para editar uma postagem existente
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)  # Recupera a postagem pelo ID ou retorna um erro 404
    if request.method == 'POST':  # Verifica se o método da requisição é POST
        form = PostForm(request.POST, instance=post)  # Cria um formulário com os dados enviados e a postagem existente
        if form.is_valid():  # Verifica se o formulário é válido
            form.save()  # Salva as alterações no banco de dados
            return redirect('post_list')  # Redireciona para a página com a lista de postagens
    else:  # Se o método da requisição não for POST
        form = PostForm(instance=post)  # Cria um formulário com os dados da postagem existente
    return render(request, 'app/post_form.html', {'form': form})  # Renderiza a página com o formulário

# View para excluir uma postagem
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete() #Exclui a postagem
    return redirect('post_list') #Redireciona para a lista de postagens após a exclusão