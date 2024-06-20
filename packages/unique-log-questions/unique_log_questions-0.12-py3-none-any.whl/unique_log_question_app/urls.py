from django.urls import path
from . import views

urlpatterns = [
    path('unique_questions/', views.display_unique_questions, name='display_questions_answers'),
    path('log_questions/', views.display_log_questions, name='display_log_answers'),
    path('new/', views.qna_create, name='qna_create'),
    path('edit/<int:pk>/', views.qna_update, name='qna_update'),
    path('delete/<int:pk>/', views.qna_delete, name='qna_delete'),
    path('delete_log/<int:pk>/', views.qna_delete_log, name='qna_delete_log'),
    
]
