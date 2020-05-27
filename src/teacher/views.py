from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
# Create your views here.
from django.urls import reverse

from teacher.forms import TeacherAddForm, TeacherEditForm
from teacher.models import Teacher


def generate_teacher(request):
    number = request.GET.get('number', 10)
    if number is not None:
        for i in range(int(number)):
            Teacher.generate_teacher()
        return HttpResponse(f'"{number}" of teachers were generated.')


def teachers_list(request):
    qs = Teacher.objects.all()
    return render(
        request=request,
        template_name='teachers_list.html',
        context={'teachers_list': qs,
                 'title': 'Teachers list'}
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
        context={'form': form, }

    )


def teachers_edit(request, id):
    try:
        teacher = Teacher.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f'Teacher with id={id} does not exists.')

    if request.method == 'POST':
        form = TeacherEditForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers'))
    else:
        form = TeacherEditForm(
            instance=teacher
        )
    return render(
        request=request,
        template_name='teachers_edit.html',
        context={'form': form,
                 'title': 'Edit teachers',
                 'teacher': teacher, }
    )


def teachers_delete(request, id):
    Teacher.objects.filter(pk=id).delete()
    return HttpResponseRedirect(reverse('teachers'))
