from django.shortcuts import render,redirect

# Create your views here.
from django.shortcuts import render, HttpResponseRedirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.views.generic import TemplateView, ListView,  CreateView,DeleteView
from django.core.files.storage import FileSystemStorage
from .forms import BookForm
from .models import Book
from django.urls import reverse_lazy


class Home(TemplateView):
    template_name = 'home.html'

def upload(request):
    context= {}
    if request.method == "POST":
        uploaded_files = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_files.name ,uploaded_files)
        context['url'] = fs.url(name)
        
        # print(uploaded_files.name)
        # print(uploaded_files.size)
    return render(request ,'upload.html',context)

def upload_book(request):
    if request.method =="POST":
        form = BookForm(request.POST,request.FILES) 
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
            form= BookForm()
    return render(request ,"upload_book.html", {'form':form})

def book_list(request):
    books = Book.objects.all()
    return render (request , "book_list.html", {'books' : books})

def delete_book(request,pk):
    if request.method =="POST":
        book= Book.objects.get(pk=pk)
        book.pdf.delete()
        book.cover.delete()
        book.delete()
 
        return redirect('book_list')

       

def delete_all_books(request):
    all_books = Book.objects.all()
    for book in all_books:
        book.pdf.delete()
        book.cover.delete()
        book.delete()
    return redirect('book_list')

class BookListView(ListView):
    model = Book
    template_name = "class_book_list.html"
    context_object_name = "books"


class UploadBookView(CreateView):
    model = Book
    # fields = ('title', 'author','pdf','cover')
    form_class = BookForm
    template_name ="upload_book.html"
    success_url = reverse_lazy("class_book_list")

class DeleteBookView(DeleteView):
    model= Book
    success_url = reverse_lazy("class_book_list")


    def delete(self,request,*args,**kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()


        self.objects.pdf.delete()
        if self.object.cover:
            self.object.cover.delete()
        self.object.delete()
        return HttpResponseRedirect(success_url)