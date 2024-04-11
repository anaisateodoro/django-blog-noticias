import pytest
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from blog.models import Post

@pytest.mark.django_db
def test_create_post():
    # Criar um usuário de teste
    author = User.objects.create_user(username='test_user', password='test_password')
    
    # Criar uma instância do modelo Post
    post = Post.objects.create(image='images/default.jpg',
                               title='Test Title',
                               slug='test-title',
                               author=author,
                               content='Test Content',
                               status=1
    )

     # Executar asserções para verificar se a instância do modelo foi criada com sucesso
    assert Post.objects.count() == 1
    assert post.title == 'Test Title'
    assert post.slug == 'test-title'
    assert post.author == author
    assert post.content == 'Test Content'
    assert post.status == 1

@pytest.mark.django_db
def test_post_str():
    # Criar um usuário de teste
   
    author = User.objects.create_user(username=
   'test_user', password='test_password'
   )
   
    # Criar uma instância do modelo Post
    post = Post.objects.create(
        image='images/default.jpg',
        title='Test Title',
        slug='test-title',
        author=author,
        content='Test Content',
        status=1
    )
    
    # Executar asserção para verificar se o método __str__ funciona conforme esperado
    assert str(post) == 'Test Title'

    def __str__(self):
        return f'{self.nome}'