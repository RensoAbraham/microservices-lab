from rest_framework import viewsets, mixins
from .models import Post
from .serializers import PostListSerializer, PostDetailSerializer

class PostViewSet(mixins.ListModelMixin, 
                  mixins.RetrieveModelMixin, 
                  viewsets.GenericViewSet):
    
    queryset = Post.objects.filter(status="published").select_related("author", "category")
    serializer_class = PostListSerializer # Serializer por defecto
    lookup_field = 'slug' # Para buscar posts por su slug en la URL

    def get_serializer_class(self):
        # Si la acción es 'retrieve' (ver detalle), usa el serializer de detalle.
        # De lo contrario, usa el de la lista.
        if self.action == 'retrieve':
            return PostDetailSerializer
        return PostListSerializer