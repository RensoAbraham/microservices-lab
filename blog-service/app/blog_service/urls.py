
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/posts/', include('blog_posts.urls')),
    path('api/categories/', include('blog_categories.urls')),
    
    path('healthz/', include('blog_core.urls')),
]