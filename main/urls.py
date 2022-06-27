from django.urls import path
from .views import HomeView, CreateBookView, UpdateBookView, BookDetailView

urlpatterns = [ 
    path('home/', HomeView.as_view(), name='home'),
    path('create/', CreateBookView.as_view(), name='create'),
    path('update/<int:pk>/', UpdateBookView.as_view(), name='update'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='detail'),
]