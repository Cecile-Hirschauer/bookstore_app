import pytest
from src.book import Book

def test_book_creation():
    book = Book("1984", "George Orwell", "978-0451524935")
    assert book.title == "1984"
    assert book.author == "George Orwell"
    assert book.isbn == "978-0451524935"

def test_book_str():
    book = Book("To Kill a Mockingbird", "Harper Lee", "978-0446310789")
    assert str(book) == "To Kill a Mockingbird by Harper Lee (ISBN: 978-0446310789)"