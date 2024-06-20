from django.shortcuts import render,redirect,get_object_or_404
from app1.models import ChatSession,SimilarQuestion


from django.shortcuts import render,redirect,get_object_or_404
from app1.models import ChatSession,SimilarQuestion
from .forms import ChatSessionForm, SimilarQuestionForm

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



def delete_chat_session(request, session_id):
    session = get_object_or_404(ChatSession, id=session_id)
    if request.method == 'POST':
        session.delete()
        return redirect('display_questions_answers')
    return HttpResponse(status=405)

def delete_log_question(request, question_id):
    question = get_object_or_404(SimilarQuestion, id=question_id)
    if request.method == 'POST':
        question.delete()
        return redirect('display_log_answers')
    return HttpResponse(status=405)



def edit_chat_session(request, session_id):
    session = get_object_or_404(ChatSession, id=session_id)
    if request.method == 'POST':
        form = ChatSessionForm(request.POST, instance=session)
        if form.is_valid():
            form.save()
            return redirect('display_questions_answers')
    else:
        form = ChatSessionForm(instance=session)
    return render(request, 'edit_chat_sessions.html', {'form': form})

def edit_similar_question(request, question_id):
    question = get_object_or_404(SimilarQuestion, id=question_id)
    if request.method == 'POST':
        form = SimilarQuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect('display_log_answers')
    else:
        form = SimilarQuestionForm(instance=question)
    return render(request, 'edit_similar_questions.html', {'form': form})


