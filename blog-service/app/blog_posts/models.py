from django.db import models
from blog_categories.models import Category
from blog_authors.models import Author 

class Post(models.Model):
    STATUS_CHOICES = (
        ('published', 'Published'),
        ('draft', 'Draft'),
    )

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    body = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='posts')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    published_at = models.DateTimeField(null=True, blank=True)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title