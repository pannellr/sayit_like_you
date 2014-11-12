from django.shortcuts import render
from django.template import RequestContext, loader
from django.views.generic.edit import FormView, CreateView
from django.core.urlresolvers import reverse_lazy
from .models import Question, Answer

def index(request):
    latest_questions = Question.objects.order_by('-created_at')[:5]
    context = {'latest_questions': latest_questions}
    return render(request, 'forum/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'forum/detail.html', {'question': question})

class NewQuestionView(CreateView):
    model = Question
    fields = ['question', 'tags']
    success_url = reverse_lazy('index')
    
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.instance.user = self.request.user
        return super(NewQuestionView, self).form_valid(form)

class NewAnswerView(CreateView):
    model = Answer
    fields = ['answer']
    success_url = reverse_lazy('index')
    
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.instance.user = self.request.user
        return super(NewAnswerView, self).form_valid(form)
