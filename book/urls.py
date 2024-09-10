from django.urls import path
from . import views
urlpatterns = [
    path('<int:pk>/', views.books_details,name='book_details'),
]