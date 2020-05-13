from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from group.forms import GroupAddForm
from group.models import Group


def generate_group(request):
    group_name = request.GET.get('gname')
    group_specialization = request.GET.get('gspecialization')
    Group.generate_group(group_name,group_specialization)
    return HttpResponse(f'"{group_name}" with {group_specialization} specialization was generated.')


def groups_list(request):
    qs = Group.objects.all()

    result = '<br>'.join(
        str(group)
        for group in qs
    )
    return render(
        request=request,
        template_name='groups_list.html',
        context={'groups_list': result}
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
