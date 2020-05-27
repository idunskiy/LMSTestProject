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
    for group in qs:
        print(group)
    return render(
        request=request,
        template_name='groups_list.html',
        context={'groups_list': qs,
                 'title': 'Groups list'}
    )


def groups_edit(request, id):
    try:
        group = Group.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f'Group with id={id} does not exists.')

    if request.method == 'POST':
        form = GroupEditForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups'))
    else:
        form = GroupEditForm(
            instance=group
        )
    return render(
        request=request,
        template_name='groups_edit.html',
        context={'form': form,
                 'title': 'Edit groups',
                 'group': group,
                 }
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


def groups_delete(request, id):
    Group.objects.filter(pk=id).delete()
    return HttpResponseRedirect(reverse('groups'))
