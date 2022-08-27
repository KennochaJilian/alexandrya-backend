from django.db import models

from common.models import Entity


class Book(Entity):
    title = models.CharField(max_length=255, verbose_name="Titre du livre")
    nb_pages = models.IntegerField(max_length=5, verbose_name="Nombre de pages")
    code_isbn = models.CharField(max_length=13, verbose_name="ISBN")
    summary = models.TextField(verbose_name="Résumé du livre")
    publication_date = models.DateTimeField(verbose_name="Date de publication")
    cover = models.URLField(verbose_name="Image de couverture")
    path = models.TextField(verbose_name="Lien du fichier")

    class Meta:
        app_label = "book"
        verbose_name = 'Livres'

    def __str__(self):
        return self.title
