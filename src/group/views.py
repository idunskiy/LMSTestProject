from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from group.forms import GroupAddForm, GroupEditForm, GroupDeleteForm
from group.models import Group


def generate_group(request):
    group_name = request.GET.get('gname')
    group_specialization = request.GET.get('gspecialization')
    Group.generate_group(group_name,group_specialization)
    return HttpResponse(f'"{group_name}" with {group_specialization} specialization was generated.')


# def groups_list(request):
#     qs = Group.objects.all()
#     for group in qs:
#         print(group)
#     return render(
#         request=request,
#         template_name='groups_list.html',
#         context={'groups_list': qs,
#                  'title': 'Groups list'}
#     )
#
#
# def groups_edit(request, id):
#     try:
#         group = Group.objects.get(id=id)
#     except ObjectDoesNotExist:
#         return HttpResponseNotFound(f'Group with id={id} does not exists.')
#
#     if request.method == 'POST':
#         form = GroupEditForm(request.POST, instance=group)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('groups'))
#     else:
#         form = GroupEditForm(
#             instance=group
#         )
#     return render(
#         request=request,
#         template_name='groups_edit.html',
#         context={'form': form,
#                  'title': 'Edit groups',
#                  'group': group,
#                  }
#     )
#
#
# def groups_add(request):
#     if request.method == 'POST':
#         form = GroupAddForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('groups'))
#     else:
#         form = GroupAddForm()
#     return render(
#         request=request,
#         template_name='groups_add.html',
#         context={'form': form}
#     )
#
#
# def groups_delete(request, id):
#     Group.objects.filter(pk=id).delete()
#     return HttpResponseRedirect(reverse('groups'))


class GroupsListView(LoginRequiredMixin, ListView):
    model = Group
    template_name = 'groups_list.html'
    context_object_name = 'groups_list'
    login_url = reverse_lazy('user_account:login')
    paginate_by = 3

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.order_by('-id')

        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['title'] = 'Groups list'
        return context


class GroupsUpdateView(LoginRequiredMixin, UpdateView):
    model = Group
    template_name = 'groups_edit.html'
    form_class = GroupEditForm
    login_url = reverse_lazy('user_account:login')

    def get_success_url(self):
        return reverse('groups:list')


class GroupsCreateView(LoginRequiredMixin, CreateView):
    model = Group
    template_name = 'groups_add.html'
    form_class = GroupAddForm
    login_url = reverse_lazy('user_account:login')

    def get_success_url(self):
        return reverse('groups:list')


class GroupsDeleteView(LoginRequiredMixin, DeleteView):
    model = Group
    template_name = 'groups_edit.html'
    form_class = GroupDeleteForm
    login_url = reverse_lazy('user_account:login')

    def get_success_url(self):
        return reverse('groups:list')
