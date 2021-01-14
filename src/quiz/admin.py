from django.contrib import admin
import nested_admin
from .models import Category, Quiz, Question, Answer


class AnswerInline(nested_admin.NestedTabularInline):  # ınline olarak hazırlıyor
    model = Answer


class QuestionInline(nested_admin.NestedTabularInline):
    model = Question
    inlines = [AnswerInline]


class QuizAdmin(nested_admin.NestedModelAdmin):
    model = Quiz
    inlines = [QuestionInline]


admin.site.register(Category)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question)
admin.site.register(Answer)
