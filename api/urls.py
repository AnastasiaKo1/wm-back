from django.urls import path
from api import views

urlpatterns = [
    path('articles/', views.Articles.as_view()),
    path('articles/publish/', views.create_article),
    path('categories/', views.categories),

]