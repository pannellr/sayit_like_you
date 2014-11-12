from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    question = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    tags = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __unicode__(self):
        return self.question
    

class Language(models.Model):
    name = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __unicode__(self):
        return self.name
    
class Answer(models.Model):
    question = models.ForeignKey(Question)
    language = models.ForeignKey(Language)
    user = models.ForeignKey(User)
    answer = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __unicode__(self):
        return self.answer
