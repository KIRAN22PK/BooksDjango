from django.shortcuts import render,get_object_or_404
from book.models import bookss

# Create your views here.
def books_details(request,pk):
    book=get_object_or_404(bookss,pk=pk)
    context={
        'book':book,
    }
    return render(request,'book_details.html',context)