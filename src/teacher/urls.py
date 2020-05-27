from django.urls import path

from teacher.views import teachers_list, teachers_add, teachers_edit, teachers_delete

urlpatterns = [
    path('', teachers_list, name='teachers'),
    path('add', teachers_add, name='teachers_add'),
    path('edit/<int:id>', teachers_edit, name='teachers_edit'),
    path('delete/<int:id>', teachers_delete, name='teachers_delete'),

]
