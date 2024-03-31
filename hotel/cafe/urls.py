from django.urls import path
from . import views

urlpatterns = [
    path('menu/<int:cafe_id>/', views.menu),
    
]
