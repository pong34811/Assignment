
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),

    path('create/', views.create),

    path('edit/<book_id>', views.edit),
    
    path('delete/<book_id>', views.delete),
]