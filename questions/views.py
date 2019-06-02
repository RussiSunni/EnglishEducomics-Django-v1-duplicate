from django.shortcuts import render
from django.template.response import TemplateResponse
from .forms import AnswerForm
from questions.models import Answer
# Create your views here.


def Fish_people_quest(request):
    data = Answer.objects.all()

    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.save()

    else:
        form = AnswerForm()
    return render(request, 'questions/answer_form.html', {'form' : form, 'data' : data})



def Fish_people_quest_answers(request):
    data = Answer.objects.all()
    return TemplateResponse(request, 'questions/Fish_people_quest_answers.html.html', {"data": data})



def ShowAnswer(request):
    data = Answer.objects.all()
    return TemplateResponse(request, 'Fish_people_quest', { "data": data })

