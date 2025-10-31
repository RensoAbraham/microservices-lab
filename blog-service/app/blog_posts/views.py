from django.db.models import Q
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import viewsets, mixins
from .models import Post
from .serializers import PostListSerializer, PostDetailSerializer


class PostViewSet(mixins.ListModelMixin, 
                  mixins.RetrieveModelMixin, 
                  viewsets.GenericViewSet):
    
    serializer_class = PostListSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        queryset = Post.objects.filter(status="published").select_related("author", "category")
        search_term = self.request.query_params.get('search', None)
        if search_term:
            queryset = queryset.filter(
                Q(title__icontains=search_term) | 
                Q(body__icontains=search_term)
            )
        return queryset

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PostDetailSerializer
        return self.serializer_class

    @method_decorator(cache_page(60 * 1), name='retrieve')
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)