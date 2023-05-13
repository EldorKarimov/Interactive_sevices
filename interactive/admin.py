from django.contrib import admin

from .models import Leader, SendData, AnswerData

admin.site.register([Leader, SendData, AnswerData])