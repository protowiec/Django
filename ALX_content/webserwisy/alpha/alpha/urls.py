from django.contrib import admin
from django.urls import path
import library.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', library.views.home, name="home"),
    path('books/add', library.views.add_book, name="add book"),
    path('books/add_modelform', library.views.add_book_modelform, name="add book with modelform"),
    path('books/<int:book_id>', library.views.book, name="book"),
    path('author/<int:author_id>', library.views.author, name="author")
]
