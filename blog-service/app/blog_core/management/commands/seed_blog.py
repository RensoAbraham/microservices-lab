import random
from django.core.management.base import BaseCommand
from faker import Faker
from slugify import slugify

from blog_authors.models import Author
from blog_categories.models import Category
from blog_posts.models import Post

class Command(BaseCommand):
    help = 'Inicia la base de datos con los datos iniciales para el blog.'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Comenzando a sembrar la base de datos...'))

        Post.objects.all().delete()
        Category.objects.all().delete()
        Author.objects.all().delete()
        self.stdout.write(self.style.WARNING('Datos antiguos borrados.'))

        fake = Faker()

        authors = []
        for _ in range(3):
            author = Author.objects.create(
                display_name=fake.name(),
                email=fake.email()
            )
            authors.append(author)
        self.stdout.write(self.style.SUCCESS(f'{len(authors)} autores creados.'))

        category_names = ['Tecnología', 'Ciencia', 'Salud', 'Viajes', 'Programación']
        categories = []
        for name in category_names:
            category = Category.objects.create(
                name=name,
                slug=slugify(name)
            )
            categories.append(category)
        self.stdout.write(self.style.SUCCESS(f'{len(categories)} categories created.'))

        posts = []
        for _ in range(30):
            title = fake.sentence(nb_words=6)
            post = Post.objects.create(
                title=title,
                slug=slugify(title),
                body=fake.text(max_nb_chars=1000),
                author=random.choice(authors),
                category=random.choice(categories),
                status=random.choice(['published', 'draft'])
            )
            posts.append(post)
        self.stdout.write(self.style.SUCCESS(f'{len(posts)} publicación creada.'))

        self.stdout.write(self.style.SUCCESS('¡Se ha completado la inicialización de la base de datos!'))