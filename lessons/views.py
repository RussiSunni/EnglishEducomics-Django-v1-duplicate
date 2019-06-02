from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.generic import TemplateView

from .models import Question
from .forms import TradeForm



def question_list(request, pk):
    template_name='lessons/question_list.html'

    def get(self, request):
        form=TradeForm()
        return render(request, self.template_name, {'form':form})




def index(request):
    return render(request, 'lessons/index.html')

def welcome(request):
    return render(request, 'lessons/welcome.html')

def home_screen(request):
    return render(request, 'lessons/home_screen.html')

def achievements(request):
    return render(request, 'lessons/achievements.html')

def useful_vocabulary(request):
    return render(request, 'lessons/useful_vocabulary.html')

def travelling(request):
    return render(request, 'lessons/travelling.html')

def travelling_ship(request):
    return render(request, 'lessons/travelling_ship.html')

def quests(request):
    return render(request, 'lessons/quests.html')

def fish_person_hello(request):
    return render(request, 'lessons/fish_person_hello.html')

def outside(request):
    return render(request, 'lessons/outside.html')

def outside_Fish_people_quest(request):
    return render(request, 'lessons/outside-Fish_people_quest.html')

def map_screen(request):
    return render(request, 'lessons/map_screen.html')

def Fisherhaven(request):
    return render(request, 'lessons/Fisherhaven.html')

#def Fish_people_quest(request):
#    return render(request, 'lessons/Fish_people_quest.html')

def thisway(request):
    return render(request, 'lessons/thisway.html')

def reception(request):
    return render(request, 'lessons/reception.html')

def docks(request):
    return render(request, 'lessons/docks.html')

def QuestFishPrincess(request):
    return render(request, 'lessons/QuestFishPrincess.html')

def QuestTannasPast(request):
    return render(request, 'lessons/QuestTannasPast.html')

def TannasPast001(request):
    return render(request, 'lessons/TannasPast001.html')

def TannasPast002(request):
    return render(request, 'lessons/TannasPast002.html')

def TannasPast003(request):
    return render(request, 'lessons/TannasPast003.html')

def FightSequence1(request):
    return render(request, 'lessons/fightsequence1.html')

def FightSequence2(request):
    return render(request, 'lessons/fightsequence2.html')

def FightSequence3(request):
    return render(request, 'lessons/fightsequence3.html')

def FightSequence4(request):
    return render(request, 'lessons/fightsequence4.html')

def FightSequence5(request):
    return render(request, 'lessons/fightsequence5.html')

def FightSequence6(request):
    return render(request, 'lessons/fightsequence6.html')










