from django.shortcuts import render,redirect,get_object_or_404
from app1.models import ChatSession,SimilarQuestion
from unique_log_question_app.forms import QnAForm

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

def qna_create(request):
    if request.method == 'POST':
        form = QnAForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = QnAForm()  # Initialize the form for GET requests
    return render(request, 'qna_form.html', {'form': form})



def qna_update(request, pk):
    qna = get_object_or_404(ChatSession, pk=pk)
    if request.method == 'POST':
        form = QnAForm(request.POST, instance=qna)
        if form.is_valid():
            form.save()
            return redirect('file_details', file_id=qna.file_id)

    else:
        form = QnAForm(instance=qna)
    return render(request, 'qna_form.html', {'form': form, 'qna': qna}) 

def qna_delete(request, pk):
    qna = get_object_or_404(ChatSession, pk=pk)
    if request.method == 'POST':  # Corrected 'methos' to 'method'
        qna.delete()
        return redirect('file_details', file_id=qna.file_id)
    return render(request, 'qna_confirm_delete.html', {'qna': qna})


def qna_delete_log(request, pk):
    qna = get_object_or_404(SimilarQuestion, pk=pk)
    if request.method == 'POST':  # Corrected 'methos' to 'method'
        qna.delete()
        return redirect('file_details_log_questions', file_id=qna.file_id)
    return render(request, 'qna_confirm_delete.html', {'qna': qna})