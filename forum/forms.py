from django.forms import ModelForm
from models import Question, Answer


class QuestionForm(ModelForm):
     class Meta:
         model = Question
         fields = ['question', 'tags']

class AnswerForm(ModelForm):
     class Meta:
         model = Answer
         fields = ['answer', 'language']
