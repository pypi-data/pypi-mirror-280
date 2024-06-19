# app1/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('unique_questions/', views.display_unique_questions, name='display_questions_answers'),
    path('log_questions/', views.display_log_questions, name='display_log_answers'),
    
]
