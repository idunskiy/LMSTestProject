"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from group.views import groups_list, groups_add, groups_edit
from student.views import generate_student, student_list, students_add, students_edit, students_delete
from teacher.views import teachers_list, teachers_add

urlpatterns = [
    path('', admin.site.urls),
    path('admin/', admin.site.urls),
    path('generate-student', generate_student),
    path('students', student_list, name='students'),
    path('students/add/', students_add, name='students_add'),
    path('students/edit/<int:id>', students_edit, name='students_edit'),
    path('students/delete/<int:id>', students_delete, name='students_delete'),
    path('groups', groups_list, name='groups'),
    path('groups/edit/<int:id>', groups_edit, name='groups_edit'),
    path('groups/add', groups_add, name='groups_add'),
    path('teachers', teachers_list, name='teachers'),
    path('teachers/add', teachers_add, name='teachers_add'),

]
