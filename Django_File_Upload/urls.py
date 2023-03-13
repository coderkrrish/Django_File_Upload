"""Django_File_Upload URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from upload import views

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home.as_view(),name = 'home'),
    path('upload/' ,views.upload, name ="upload"),
    path("books/", views.book_list, name= "book_list"),
    path("delete/<int:pk>/",views.delete_book,name = "delete_book"),
    path('delete-all/', views.delete_all_books, name = 'delete-all'),
    path("books/upload/",views.upload_book,name='upload_book'),
    path("class/books/", views.BookListView.as_view(),name = "class_book_list"),
    path("class/upload/",views.UploadBookView.as_view(),name = "class_book_upload")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
