from django.urls import path
from .views import BookClassView, book_function_view

urlpatterns = [
    path('book_class_view', BookClassView.as_view(), name='book_class_view'), #class based view URL
    path('book_function_view', book_function_view, name='book_function_view'),#function based view URL
    
]