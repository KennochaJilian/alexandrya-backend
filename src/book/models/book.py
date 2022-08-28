from django.db import models

from book.models.author import Author
from book.models.category import Category
from common.models import Entity


class Book(Entity):
    title = models.CharField(max_length=255, verbose_name="Titre du livre")
    nb_pages = models.IntegerField(verbose_name="Nombre de pages", null=True)
    summary = models.TextField(verbose_name="Résumé du livre", null=True)
    publication_date = models.DateTimeField(verbose_name="Date de publication")
    cover = models.URLField(verbose_name="Image de couverture", null=True)
    path = models.TextField(verbose_name="Lien du fichier")
    authors = models.ManyToManyField(Author, related_name="books")
    categories = models.ManyToManyField(Category, related_name="books")

    class Meta:
        app_label = "book"
        verbose_name = 'Livres'

    def __str__(self):
        return self.title
