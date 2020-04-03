from django.db.models import Q
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from books.models import Book


class BooksListView(LoginRequiredMixin, generic.ListView):
    login_url = 'account_login'
    model = Book
    template_name = 'books/books_list.html'
    context_object_name = 'books'


class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, generic.DetailView):
    login_url = 'account_login'  # used for LoginRequiredMixin
    model = Book
    template_name = 'books/books_detail.html'
    context_object_name = 'book'
    permission_required = "books.special_status"  # used for PermissionRequiredMixin


class SearchResultsListView(generic.ListView):
    model = Book
    template_name = 'books/search_results.html'
    context_object_name = 'book_list'

    # def get_queryset(self):
    #     return Book.objects.filter(
    #         Q(title__icontains='Beginner') | Q(title__contains='Fake')
    #     )  # Note that icontains is not case sensitive but contains is ;)
    def get_queryset(self):
        query = self.request.GET.get('q')
        return Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
