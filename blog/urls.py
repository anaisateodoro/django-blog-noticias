from django.contrib.sitemaps.views import sitemap
from . import views
from django.urls import path,include
from .feeds import LatestPostFeed
from oursite.sitemaps import PostSitemap
from django.conf.urls.static import static

# Sitemap configuration
sitemaps = {
    "posts": PostSitemap,
}

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('search/', views.search, name='search'),
    path('nossa_missao/', views.NossaMissaoView.as_view(), name='nossa_missao'),
    path('sobre/', views.Sobre.as_view(), name='sobre'),
    path('contato/', views.ContatoCreate.as_view(), name='contato_form'),
    path('sucesso/', views.ContatoCreateSuccess.as_view(), name='contato_form_success'),
    path('summernote/', include('django_summernote.urls')),
    path('feed/rss',LatestPostFeed(), name='post_feed'),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
    path('cadastro/', views.cadastro_autor, name='cadastro_autor'),
    path('login/', views.login_autor, name='login_autor'),
    path('logado/', views.autor_logado, name='autor_logado'),
    path('logout/', views.logout_autor, name='logout_autor'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]


