# Crear noosas views aqui.
from django.views import generic
from .models import Post
from .forms import CommentForm
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect




class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


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

@require_POST
def post_comment(request, slug):
    post = Post.objects.get(slug=slug)
    comment_form = CommentForm(data=request.POST)
    if comment_form.is_valid():
        post.comments.create(**comment_form.cleaned_data)
    return redirect('post_detail', slug=slug)