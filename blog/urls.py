from . import views
from django.urls import path
from django.contrib.sitemaps.views import sitemap #Sitemap view
from oursite.sitemaps import PostSitemap   #Sitemap view


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]

# Sitemap configuration
sitemaps = {
    "posts": PostSitemap,
}
urlpatterns = [
        
.......... 
   path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),        
.........]
