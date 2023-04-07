from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from django101.web.models import Todo


def index(request):
    context = {
        'title': 'Function-based view'
    }

    return render(request, 'index.html', context)


class IndexView(views.View):
    def get(self, request):
        context = {
            'title': 'Class-based view',
        }

        return render(request, 'index.html', context)


class IndexTemplateViewBased(views.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Class-based with TemplateView'
        return context


class IndexTemplateViewChild(IndexTemplateViewBased):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title2'] = 'Class-based with TemplateView Inherited'
        return context


class TodosListView(views.ListView):
    model = Todo
    template_name = 'todos-list.html'
    ordering = ('title', 'category__name')


class TodoDetailView(views.DetailView):
    model = Todo
    template_name = 'todo-details.html'


# class RedirectToIndexView(views.RedirectView):
#     url = reverse_lazy('class-based index')

class TodoCreateView(views.CreateView):
    model = Todo
    template_name = 'todo-create.html'
    success_url = reverse_lazy('todos list')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Todo Form'
        return context