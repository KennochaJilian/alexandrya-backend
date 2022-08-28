from book.models.book import Book
from common.serializers.entity import EntitySerializer


class ListBookSerializer(EntitySerializer):
    class Meta:
        model = Book
        field = "__all__"
