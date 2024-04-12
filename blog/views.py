# Crear noosas views aqui.
from django.views import generic
from .models import Post, Contato, Autor
from .forms import CommentForm , ContatoForm, AutorForm, PostForm
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.contrib.auth import logout
from django.contrib import messages 

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 3


def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = Post.objects.get(slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    comment_form = CommentForm()
    
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = post.comments.create(**comment_form.cleaned_data)

    return render(request, template_name, {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
    })
    
def search(request):
    query = request.GET.get('q')
    results = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
    return render(request, 'search_results.html', {'results': results})

@require_POST
def post_comment(request, slug):
    post = Post.objects.get(slug)
    comment_form = CommentForm(data=request.POST)
    if comment_form.is_valid():
        post.comments.create(**comment_form.cleaned_data)
    return redirect('post_detail', slug=slug)


class ContatoCreate(CreateView):
    form_class = ContatoForm
    template_name = 'contato.html'

    
    def get_success_url(self):
        return reverse('contato_form_success')

class ContatoCreateSuccess(TemplateView):
    template_name = 'contato_success.html'


class NossaMissaoView(TemplateView):
    template_name = 'nossa_missao.html'
    

class Sobre(TemplateView):
    template_name = 'sobre.html'


def cadastro_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_autor')  # Redireciona para a página de login
    else:
        form = AutorForm()
    return render(request, 'cadastro_autor.html', {'form': form})

def login_autor(request):
    if request.method == 'POST' and 'email' in request.POST:
        email = request.POST['email'].strip()
        senha = request.POST['senha'].strip()
       
        autor = Autor.objects.filter(email=email, senha=senha).first()
        if autor is not None:
            return redirect('autor_logado')
        else:
            return render(request, 'login_autor.html', {'erro': True})
    else:
        return render(request, 'login_autor.html')
    
def autor_logado(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
        # Save the post instance with the logged-in author
            post = form.save(commit=False)  # Don't commit yet
            post.author = request.user  # Assign the logged-in author
            post.save()  # Now save the post with the author
            return redirect('autor_logado')
    else:
        form = PostForm()
    return render(request, 'autor_logado.html', {'form': form})

def logout_autor(request):
    logout(request)
    return redirect('home')