from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response

from book.extract_metadata import save_books
from book.models.book import Book
from book.serializers.book_serializer import ListBookSerializer


class BookViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Book.objects.first()
    serializer_class = ListBookSerializer

    @action(methods=['GET'], detail=False, url_path='extract')
    def get_me(self, request):
        save_books()
        return Response("Ok !", status=status.HTTP_200_OK)
