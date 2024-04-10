from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime
from django.utils.html import format_html


# Criar nossas models aqui.

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("post_detail", kwargs={"slug": str(self.slug)})

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=200, verbose_name='nome')
    email = models.EmailField(verbose_name='email')
    body = models.TextField(verbose_name='comentário')
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
    
class Contato(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(verbose_name='email')
    telefone = models.CharField(null=True, blank=True)
    assunto = models.CharField(max_length=100)
    mensagem = models.TextField(verbose_name='deixe sua mensagem')

    class Meta:
        verbose_name = 'Contato'
        ordering = ['-data']
        
    def __str__(self):
        return self.nome