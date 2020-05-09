from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from group.models import Group


def generate_group(request):
    group_name = request.GET.get('gname')
    group_specialization = request.GET.get('gspecialization')
    Group.generate_group(group_name,group_specialization)
    return HttpResponse(f'"{group_name}" with {group_specialization} specialization was generated.')

    # return render(
    #     request=request,
    #     template_name='groups_add.html',
    # )


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
