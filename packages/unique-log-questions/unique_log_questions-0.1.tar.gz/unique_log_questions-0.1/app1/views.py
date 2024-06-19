from django.shortcuts import render,redirect,get_object_or_404
from app1.models import ChatSession,SimilarQuestion


def display_unique_questions(request):
    chat_sessions = ChatSession.objects.all()
    
    context = {
        'chat_sessions': chat_sessions
    }
    return render(request, 'unique_questions.html', context)


def display_log_questions(request):
    
    similar_questions = SimilarQuestion.objects.all()

    context = {
        
        'similar_questions': similar_questions
    }
    return render(request, 'log_questions.html', context)