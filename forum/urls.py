from django.conf.urls import patterns, url

from forum import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
    url(r'question/new/$', views.NewQuestionView.as_view(), name='new_question'),
    url(r'question/(?P<question_id>\d+)/answer/new/$', views.NewAnswerView.as_view(), name='new_answer'),
)
