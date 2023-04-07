from django.urls import path

from django101.web.views import index, IndexView, IndexTemplateViewBased, IndexTemplateViewChild, TodosListView, \
    TodoDetailView, TodoCreateView

urlpatterns = [
    path('', index, name='function-based index'),
    path('cbv/', IndexView.as_view(), name='class-based index'),
    path('cbv/template/', IndexTemplateViewBased.as_view(), name='class-based index (templated)'),
    path('cbv/template2/', IndexTemplateViewChild.as_view(), name='class-based index (templated) inherited'),
    path('todos-list/', TodosListView.as_view(), name='todos list'),
    path('todos-details/<int:pk>/', TodoDetailView.as_view(), name='todos details'),
    path('todos/create/', TodoCreateView.as_view(), name='create todo'),

]