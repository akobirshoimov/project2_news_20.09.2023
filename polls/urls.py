from django.urls import path
from .views import CreateNewsView,UpdateNewsView,ListNewsView

urlpatterns = [
    path('all/',ListNewsView.as_view()),
    path('create/<int:news_id>/',CreateNewsView.as_view()),
    path('update/',UpdateNewsView.as_view())
]