# Crear noosas views aqui.
from django.views import generic
from .models import Post, Contato
from .forms import CommentForm , ContatoForm
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView



class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 2


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
    post = Post.objects.get(slug=slug)
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