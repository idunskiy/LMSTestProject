from django.urls import path

from group.views import GroupsListView, GroupsUpdateView, \
    GroupsDeleteView, GroupsCreateView

app_name = 'groups'

urlpatterns = [
    path('', GroupsListView.as_view(), name='list'),
    path('edit/<int:pk>', GroupsUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>', GroupsDeleteView.as_view(), name='delete'),
    path('add', GroupsCreateView.as_view(), name='add'),

]
