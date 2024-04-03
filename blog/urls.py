from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('feed/rss',LatestPostFeed(), name='post_feed'),
]

# Sitemap configuration
sitemaps = {
    "posts": PostSitemap,
}
urlpatterns = [
        
.......... 
   path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),        
.........]
