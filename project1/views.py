from django.shortcuts import render
from book.models import bookss
def information(request):
    book=bookss.objects.all()
    context={
        'book':book,
    }
    return render(request,'home.html',context)