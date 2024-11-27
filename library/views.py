from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, FileResponse
from .models import User, Book
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        remember_me = request.POST.get('remember_me', False)

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if remember_me:
                request.session.set_expiry(7 * 24 * 60 * 60)
            else:
                request.session.set_expiry(0)
            return redirect('books')
        else:
            return JsonResponse({"error": "Invalid credentials"}, status=400)
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def list_books(request):
    books = Book.objects.all()
    return JsonResponse({"books": list(books.values())})

@login_required
def add_book(request):
    if request.user.role != 'admin':
        return JsonResponse({"error": "Unauthorized access"}, status=403)
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        description = request.POST['description']
        file = request.FILES['file']
        Book.objects.create(title=title, author=author, description=description, file=file)
        return JsonResponse({"message": "Book added successfully"})

@login_required
def update_book(request, book_id):
    if request.user.role != 'admin':
        return JsonResponse({"error": "Unauthorized access"}, status=403)
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'PUT':
        book.title = request.PUT.get('title', book.title)
        book.author = request.PUT.get('author', book.author)
        book.description = request.PUT.get('description', book.description)
        book.save()
        return JsonResponse({"message": "Book updated successfully"})

@login_required
def delete_book(request, book_id):
    if request.user.role != 'admin':
        return JsonResponse({"error": "Unauthorized access"}, status=403)
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return JsonResponse({"message": "Book deleted successfully"})

@login_required
def download_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return FileResponse(book.file, as_attachment=True, filename=book.file.name)
