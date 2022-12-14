from django.urls import path
from .views import ProductView, ProductCreate, ProductDelete, ProductUpdate

urlpatterns = [
    path('', ProductView.as_view()),
    path('create/', ProductCreate.as_view()),
    path('delete/', ProductDelete.as_view()),
    path('update/', ProductUpdate.as_view()),
]
