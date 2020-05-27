from django.urls import path

from group.views import groups_list, groups_add, groups_edit, groups_delete

urlpatterns = [
    path('', groups_list, name='groups'),
    path('edit/<int:id>', groups_edit, name='groups_edit'),
    path('delete/<int:id>', groups_delete, name='groups_delete'),
    path('add', groups_add, name='groups_add'),

]
