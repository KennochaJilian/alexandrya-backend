from django.urls import path, include
from rest_framework_nested import routers

from book.views.book_viewset import BookViewSet

router = routers.DefaultRouter()

router.register('books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
