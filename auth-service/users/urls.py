from djoser import views as djoser_views
from django.urls import path
from .views import RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('me/', djoser_views.UserViewSet.as_view({'get': 'me'}), name='user-me'),
]