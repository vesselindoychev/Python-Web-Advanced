from django.db.models import Model
from django.shortcuts import render
from django.views import generic as views
from exceptions_demos.web.models import Todo


class HomeView(views.TemplateView):
    template_name = 'index.html'


class InternalErrorView(views.View):
    raise TypeError

def todo_by_id(pk):
    try:
        todo = Todo.objects.get(pk=pk)
    except Model.DoesNotExist:
        pass

    todo = Todo.objects.filter(pk=pk)
    if not todo:
        pass
