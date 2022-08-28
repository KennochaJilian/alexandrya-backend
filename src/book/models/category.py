from django.db import models

from common.models import Entity


class Category(Entity):
    name = models.CharField(max_length=255, verbose_name="Nom catégorie")

    class Meta:
        app_label = "book"
        verbose_name = 'Categorie'

    def __str__(self):
        return self.name
