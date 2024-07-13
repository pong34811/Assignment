from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Book

# Create your views here.

def home(request):
    book = Book.objects.all()
    return render(request, 'index.html', {'book': book})

def create (request):
    if request.method == 'POST':
        book_name_th = request.POST['book_name_th']
        book_name_en = request.POST['book_name_en']
        number_si = request.POST['number_si']
        datetime = request.POST['datetime']
        detail_book = request.POST['detail_book']
        bookshop = request.POST['bookshop']
        sale_book = request.POST['sale_book']
        print = (book_name_th, book_name_en, number_si, datetime, detail_book, bookshop, sale_book)

        book = Book.objects.create(
            book_name_th = book_name_th,
            book_name_en = book_name_en,
            number_si =  number_si,
            datetime = datetime,
            detail_book = detail_book,
            bookshop = bookshop,
            sale_book = sale_book,
        )
        book.save()

        messages.success(request, "Successfully")

        return redirect('/')

    
    return render(request, 'create.html')

def edit (request, book_id):
    
    if request.method == 'POST':
        book_name_th = request.POST['book_name_th']
        book_name_en = request.POST['book_name_en']
        number_si = request.POST['number_si']
        datetime = request.POST['datetime']
        detail_book = request.POST['detail_book']
        bookshop = request.POST['bookshop']
        sale_book = request.POST['sale_book']
        print = (book_name_th, book_name_en, number_si, datetime, detail_book, bookshop, sale_book)

        book = Book.objects.get(id=book_id)
        book.book_name_th = book_name_th
        book.book_name_en = book_name_en
        book.number_si =  number_si
        book.datetime = datetime
        book.detail_book = detail_book
        book.bookshop = bookshop
        book.sale_book = sale_book

        book.save()

        messages.success(request, "Successfully EDIT")

        return redirect('/')
    else:
        book = Book.objects.get(id=book_id)
        return render(request, 'edit.html', {'book': book})
    
def delete (request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    messages.success(request, "Successfully DELETE")
    return redirect('/')