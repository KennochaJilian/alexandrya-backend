from rest_framework import viewsets, mixins

from book.models.books import Book
from book.serializers.book_serializer import ListBookSerializer


class BookViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Book.objects.all()
    serializer_class = ListBookSerializer
