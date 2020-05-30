from django.urls import path

from teacher.views import TeachersListView, \
    TeachersCreateView, TeachersDeleteView, TeachersUpdateView

app_name = 'teachers'

urlpatterns = [
    path('', TeachersListView.as_view(), name='list'),
    path('add', TeachersCreateView.as_view(), name='add'),
    path('edit/<int:pk>', TeachersUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>', TeachersDeleteView.as_view(), name='delete'),

]
