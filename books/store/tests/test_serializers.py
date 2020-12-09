from django.test import TestCase

from store.models import Book
from store.serializers import BookSerializer


class BookSerializerTest(TestCase):
    def setUp(self):
        self.book_1 = Book.objects.create(name='Test book 1', price=25, author_name='Author 1')
        self.book_2 = Book.objects.create(name='Test book 2', price=75, author_name='Author 5')
        self.book_3 = Book.objects.create(name='Test book 3 Author 1', price=275, author_name='Author 2')

    def test_ok(self):
        data = BookSerializer([self.book_1, self.book_2, self.book_3], many=True).data
        expected_data = [
            {
                'id': self.book_1.id,
                'name': 'Test book 1',
                'price': '25.00',
                'author_name': 'Author 1'
            },
            {
                'id': self.book_2.id,
                'name': 'Test book 2',
                'price': '75.00',
                'author_name': 'Author 5'
            },
            {
                'id': self.book_3.id,
                'name': 'Test book 3 Author 1',
                'price': '275.00',
                'author_name': 'Author 2'
            }
        ]
        self.assertEqual(data, expected_data)
