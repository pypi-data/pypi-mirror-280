from app1.models import ChatSession
from django import forms
class QnAForm(forms.ModelForm):
    class Meta:
        model = ChatSession
        fields = ['question', 'answer']