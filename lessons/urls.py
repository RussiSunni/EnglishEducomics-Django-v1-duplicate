from django.conf.urls import url

from . import views

from questions.views import Fish_people_quest


urlpatterns = [

    url(r'^$', views.index, name='index'),

    url('welcome', views.welcome, name='welcome'),
    url(r'^home_screen', views.home_screen, name='home_screen'),
    url('achievements', views.achievements, name='achievements'),
    url('useful_vocabulary', views.useful_vocabulary, name='useful_vocabulary'),
    url('travelling_ship', views.travelling_ship, name='travelling_ship'),
    url('travelling', views.travelling, name='travelling'),
    url('quests', views.quests, name='quests'),
    url('fish_person_hello', views.fish_person_hello, name='fish_person_hello'),
    url('thisway', views.thisway, name='thisway'),
    url('outside_Fish_people_quest', views.outside_Fish_people_quest, name='outside_Fish_people_quest'),
    url('outside', views.outside, name='outside'),
    url('map_screen', views.map_screen, name='map_screen'),
    url('Fisherhaven', views.Fisherhaven, name='Fisherhaven'),
    url('Fish_people_quest', Fish_people_quest, name='Fish_people_quest'),
    url('question_list', views.question_list, name='question_list'),
    url('reception', views.reception, name='reception'),
    url('docks', views.docks, name='docks'),
#    url('HomeView', views.HomeView, name='HomeView'),
    url('QuestFishPrincess', views.QuestFishPrincess, name='QuestFishPrincess'),
    url('QuestTannasPast', views.QuestTannasPast, name='QuestTannasPast'),
    url('TannasPast001', views.TannasPast001, name='TannasPast001'),
    url('TannasPast002', views.TannasPast002, name='TannasPast002'),
    url('TannasPast003', views.TannasPast003, name='TannasPast003'),
    url('FightSequence1', views.FightSequence1, name='FightSequence1'),
    url('FightSequence2', views.FightSequence2, name='FightSequence2'),
    url('FightSequence3', views.FightSequence3, name='FightSequence3'),
    url('FightSequence4', views.FightSequence4, name='FightSequence4'),
    url('FightSequence5', views.FightSequence5, name='FightSequence5'),
    url('FightSequence6', views.FightSequence6, name='FightSequence6'),

]