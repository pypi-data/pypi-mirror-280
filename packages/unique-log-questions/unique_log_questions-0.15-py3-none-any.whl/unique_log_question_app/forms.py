
from django import forms

from app1.models import ChatSession, SimilarQuestion

class ChatSessionForm(forms.ModelForm):
    class Meta:
        model = ChatSession
        fields = ['user_name', 'question', 'answer']

class SimilarQuestionForm(forms.ModelForm):
    class Meta:
        model = SimilarQuestion
        fields = ['user_name', 'question', 'answer']
