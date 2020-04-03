from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.BooksListView.as_view(), name='books_list'),
    path('detail/<uuid:pk>/', views.BookDetailView.as_view(), name='books_detail'),
    path('search/', views.SearchResultsListView.as_view(), name='search_results'),
]
