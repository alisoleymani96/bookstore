from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.test import TestCase, Client
from django.urls import reverse

from books.models import Book, Review


class BookTest(TestCase):

    def setUp(self) -> None:
        self.book = Book.objects.create(
            title="Harry Potter",
            author="JK Rowling",
            price="25.00",
        )

        self.special_permission = Permission.objects.get(codename='special_status')

        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@mail.com',
            password='testpassword',
        )

        self.review = Review.objects.create(
            book=self.book,
            review='Awesome',
            author=self.user,
        )

    def test_book_listing(self):
        self.assertEqual(f'{self.book.title}', 'Harry Potter')
        self.assertEqual(f'{self.book.author}', 'JK Rowling')
        self.assertEqual(f'{self.book.price}', '25.00')

    def test_book_list_view_logged_in_user(self):
        self.client.login(email='test@mail.com', password='testpassword')
        response = self.client.get(reverse('books:books_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Harry Potter')
        self.assertTemplateUsed(response, 'books/books_list.html')

    def test_book_list_view_logged_out_user(self):
        self.client.logout()
        response = self.client.get(reverse('books:books_list'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, '{}?next=/books/'.format(reverse('account_login'))
        )
        response = self.client.get(
            '{}?next=/books/'.format(reverse('account_login'))
        )
        self.assertContains(response, 'login')

    def test_book_detail_view_with_permissions(self):
        self.client.login(email='test@mail.com', password='testpassword')
        self.user.user_permissions.add(self.special_permission)
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get('/books/215/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'JK Rowling')
        self.assertContains(response, '25.00')
        self.assertContains(response, 'Awesome')
        self.assertTemplateUsed(response, 'books/books_detail.html')

