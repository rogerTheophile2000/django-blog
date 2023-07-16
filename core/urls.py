from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home" ),
    path('article_add/', views.addArticle, name="article_add")
]
