from __future__ import unicode_literals

from django.db import models


from django.contrib.auth.models import User

# Create your models here.


class Answer(models.Model):
    answer = models.CharField(max_length=255, default='', blank='True')
#    user = models.ForeignKey(User)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.answer
