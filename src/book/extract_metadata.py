import glob

import epub_meta
import requests
from dateutil import parser

from book.models.author import Author
from book.models.book import Book
from book.models.category import Category

EBOOKS_PATH_DIR = "/ebooks"
PATH_GOOGLE_BOOK_API = "https://www.googleapis.com/books/v1/volumes?q="


def get_metadata_from_epub(path):
    try:
        meta_data = epub_meta.get_epub_metadata(path, read_cover_image=False)
        return meta_data
    except:
        print(path)


def get_book_data_from_google(title, author=None, publisher=None):
    url = PATH_GOOGLE_BOOK_API + title

    if author is not None:
        url += f'+inauthor:{author}'

    if publisher is not None:
        url += f'+inpublisher:{publisher}'

    response = requests.get(url)

    if response.status_code in range(300, 550):
        raise Exception

    response = response.json()
    return response


def get_google_data_from_epub(metadata):
    try:
        ebooks_from_google = get_book_data_from_google(
            metadata.get('title'),
            metadata.get('authors')[0],
            metadata.get('publisher')
        )
        items = ebooks_from_google.get('items')
        if items is None:
            return None
        volume_info = items[0].get('volumeInfo')
        if volume_info is None:
            return None

        return ebooks_from_google.get('items')[0].get('volumeInfo')

    except:
        print(metadata)


def save_authors(list_authors):
    authors = list()
    for author_name in list_authors:
        author, _ = Author.objects.get_or_create(name=author_name)
        authors.append(author)
    return authors

def save_categories(list_categories):
    categories = list()
    for category_name in list_categories:
        category, _ = Category.objects.get_or_create(name=category_name)
        categories.append(category)
    return categories

def save_book_google_data(path, book_data):
    book = Book.objects.create(
        title=book_data.get('title'),
        summary=book_data.get('description'),
        nb_pages=book_data.get('pageCount'),
        path=path,
        cover="https://widgetopia.io/widget/stitch-sSv",
        publication_date=parser.parse(book_data.get('publishedDate', '2022'))
    )

    authors = save_authors(book_data.get('authors'))
    book.authors.add(*authors)

    if book_data.get('categories') is not None:
        categories = save_categories(book_data.get('categories'))
        book.categories.add(*categories)

def save_book_epub_data(path, book_meta_data):
    published_date = book_meta_data.get('publication_date')
    if published_date is None:
        published_date = parser.parse("2022")
    else:
        published_date = parser.parse(published_date)

    book = Book.objects.create(
        title=book_meta_data.get('title'),
        path=path,
        cover="https://widgetopia.io/widget/stitch-sSv",
        publication_date=published_date
    )
    authors = save_authors(book_meta_data.get('authors'))
    book.authors.add(*authors)

    if book_meta_data.get('subject') is not None:
        categories = save_categories(book_meta_data.get('subject'))
        book.categories.add(*categories)


def save_books():
    for filename in glob.iglob(EBOOKS_PATH_DIR + '**/**', recursive=True):
        if filename.endswith('.epub'):
            try:
                book_data = get_metadata_from_epub(filename)
                if book_data is None:
                    raise Exception

                google_data = get_google_data_from_epub(book_data)

                if not Book.objects.filter(path=filename).exists():
                    if google_data is not None:
                        save_book_google_data(filename, google_data)
                        continue
                    if book_data is not None:
                        save_book_epub_data(filename, book_data)
                        continue
            except:
                print(filename)
