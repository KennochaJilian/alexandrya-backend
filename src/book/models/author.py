from django.db import models

from common.models import Entity


class Author(Entity):
    name = models.CharField(max_length=255, verbose_name="Prénom")
    biography = models.TextField(verbose_name="Biographie", null=True)
    photo = models.URLField(verbose_name="Photo", null=True)

    class Meta:
        app_label = "book"
        verbose_name = 'Auteur'

    def __str__(self):
        return self.name
