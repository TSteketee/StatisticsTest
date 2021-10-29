from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from random import randint



def question_view(request, *args, **kwargs):
    obj = Question.objects.get(id=randint(1,52))
    context = {
        "question": obj.question,
        "answer": obj.answer
    }

    return render(request, 'home.html', context)