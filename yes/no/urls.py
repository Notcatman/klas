from django.urls import path
from . import views

urlpatterns = [
    path('authors/', views.AuthorAPIView.as_view(), name='authors'),
    path('books/', views.BookAPIView.as_view(), name='books'),
]