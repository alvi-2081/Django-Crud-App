from django.contrib import admin

from .models import Question, Choice, Todo

admin.site.register([Question, Choice, Todo])
