from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from BookManagement.models import *

# Create your views here.
def Books(request):
    books = []
    if 'search' in request.GET and request.GET['search']:
        s = request.GET['search']
        Au = Author.objects.filter(Name = s)
        for a in Au:
            books += Book.objects.filter(AuthorID = a.AuthorID)
    if request.method == 'POST':
        if request.POST.get('delete'):
            s = request.POST.get('delete')
            b = Book.objects.get(ISBN = s)
            b.delete()
    return render_to_response('Books.html',{'books':books})

def book(request,BookId):
    book = Book.objects.get(ISBN = BookId)
    author = Author.objects.get(AuthorID = book.AuthorID)
    return render_to_response('Book.html',locals())

def CreateBook(request):
    error = False
    NoAuthor = False
    if request.method == 'POST':
        if request.POST.get('Title','') and request.POST.get('AuthorID','') and \
        request.POST.get('Publisher','') and request.POST.get('PublishDate','') and \
        request.POST.get('Price',''):
            if Author.objects.filter(AuthorID = request.POST.get('AuthorID')):
                b = Book(Title = request.POST.get('Title'),
                         AuthorID = request.POST.get('AuthorID'),
	                     Publisher = request.POST.get('Publisher'),
	                     PublishDate = request.POST.get('PublishDate'),
	                     Price = request.POST.get('Price'))
                b.save()
            else:
                NoAuthor = True
        else:
            error = True
    return render_to_response('CreateBook.html',{'error':error,'NoAuthor':NoAuthor})

def CreateAuthor(request):
    error = False
    if request.method == 'POST':
        if request.POST.get('AuthorID','') and request.POST.get('Name','')\
         and request.POST.get('Age','') and request.POST.get('Country',''):
            a = Author(AuthorID = request.POST.get('AuthorID'),
	                   Name = request.POST.get('Name'),
	                   Age = request.POST.get('Age'),
	                   Country = request.POST.get('Country'))
            a.save()
        else:
            error = True
    return render_to_response('CreateAuthor.html',{'error':error})

def Update(request,BookId):
    NoAuthor = False
    b = Book.objects.filter(ISBN = BookId)
    if request.method == 'POST':
        if request.POST.get('AuthorID',''):
            if Author.objects.filter(AuthorID = request.POST.get('AuthorID')):
                b.update(AuthorID = request.POST.get('AuthorID'))
            else:
                NoAuthor = True
        if request.POST.get('Publisher',''):
            b.update(Publisher = request.POST.get('Publisher'))
        if request.POST.get('PublishDate',''):
            b.update(PublishDate = request.POST.get('PublishDate'))
        if request.POST.get('Price',''):
            b.update(Price = request.POST.get('Price'))
    return render_to_response('Update.html',{'book':b[0],'NoAuthor':NoAuthor})

def Hello(request):
    return render_to_response('Hello.html')
