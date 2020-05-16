from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from group.forms import GroupAddForm, GroupEditForm
from group.models import Group


def generate_group(request):
    group_name = request.GET.get('gname')
    group_specialization = request.GET.get('gspecialization')
    Group.generate_group(group_name,group_specialization)
    return HttpResponse(f'"{group_name}" with {group_specialization} specialization was generated.')


def groups_list(request):
    qs = Group.objects.all()
    return render(
        request=request,
        template_name='groups_list.html',
        context={'groups_list': qs}
    )


def groups_edit(request, id):
    try:
        student = Group.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f'Student with id={id} does not exists.')

    if request.method == 'POST':
        form = GroupEditForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students'))
    else:
        form = GroupEditForm(
            instance=student
        )
    return render(
        request=request,
        template_name='students_edit.html',
        context={'form': form,
                 'title': 'Edit students'}
    )


def groups_add(request):
    if request.method == 'POST':
        form = GroupAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups'))
    else:
        form = GroupAddForm()
    return render(
        request=request,
        template_name='groups_add.html',
        context={'form': form}
    )
