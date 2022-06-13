from django.views.generic import ListView
from .models import Book
from django.shortcuts import render
from django.core.paginator import Paginator

#Class Based View
class BookClassView(ListView):
    model = Book
    template_name = "books.html" 
    paginate_by = 3 #Show 3 contents per page.

#Function Based View
def book_function_view(request):
    books = Book.objects.all()
    paginator = Paginator(books, 3) #Show 3 contents per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'books.html', { 'page_obj': page_obj })
    