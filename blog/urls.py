from django.contrib.sitemaps.views import sitemap
from . import views
from django.urls import path
from .feeds import LatestPostFeed
from oursite.sitemaps import PostSitemap

# Sitemap configuration
sitemaps = {
    "posts": PostSitemap,
}

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('feed/rss',LatestPostFeed(), name='post_feed'),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
]
