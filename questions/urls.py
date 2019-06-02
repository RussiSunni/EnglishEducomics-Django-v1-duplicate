from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'Fish_people_quest_answers/$', views.Fish_people_quest_answers, name='Fish_people_quest_answers'),
    url(r'Fish_people_quest/$', views.Fish_people_quest, name='Fish_people_quest'),
    url(r'show_answer/$', views.ShowAnswer, name='ShowAnswer'),


    ]