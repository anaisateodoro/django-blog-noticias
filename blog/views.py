# Crear nossas views aqui.
from django.views import generic
from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Post

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 3

    def index(request):
        post_list = Post.objects.all()
        paginator = Paginator(post_list, 5) # 5 post por página
        page_list = request.GET.get('page')
        page = page.get_page(page_list)
class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
