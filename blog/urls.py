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
    path('contato/', views.ContatoCreate.as_view(), name='contato_form'),
    path('sucesso/', views.ContatoCreateSuccess.as_view(), name='contato_form_success'),
    path('summernote/', include('django_summernote.urls')),
    path('feed/rss',LatestPostFeed(), name='post_feed'),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]


