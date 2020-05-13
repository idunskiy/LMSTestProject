from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from teacher.forms import TeacherAddForm
from teacher.models import Teacher


def generate_teacher(request):
    number = request.GET.get('number', 10)
    if number is not None:
        for i in range(int(number)):
            Teacher.generate_teacher()
        return HttpResponse(f'"{number}" of teachers were generated.')


def teachers_list(request):
    qs = Teacher.objects.all()
    result = '<br>'.join(
        str(teacher)
        for teacher in qs
    )
    return render(
        request=request,
        template_name='teachers_list.html',
        context={'teachers_list': result}
    )


def teachers_add(request):
    if request.method == 'POST':
        form = TeacherAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers'))
    else:
        form = TeacherAddForm()
    print(form)
    return render(
        request=request,
        template_name='teachers_add.html',
        context={'form': form}
    )
