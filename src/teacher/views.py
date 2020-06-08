from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, ListView

from teacher.forms import TeacherAddForm, TeacherEditForm, TeacherDeleteForm
from teacher.models import Teacher


def generate_teacher(request):
    number = request.GET.get('number', 10)
    if number is not None:
        for i in range(int(number)):
            Teacher.generate_teacher()
        return HttpResponse(f'"{number}" of teachers were generated.')


# def teachers_list(request):
#     qs = Teacher.objects.all()
#     return render(
#         request=request,
#         template_name='teachers_list.html',
#         context={'teachers_list': qs,
#                  'title': 'Teachers list'}
#     )
#
#
# def teachers_add(request):
#     if request.method == 'POST':
#         form = TeacherAddForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('teachers'))
#     else:
#         form = TeacherAddForm()
#     print(form)
#     return render(
#         request=request,
#         template_name='teachers_add.html',
#         context={'form': form, }
#
#     )
#
#
# def teachers_edit(request, id):
#     try:
#         teacher = Teacher.objects.get(id=id)
#     except ObjectDoesNotExist:
#         return HttpResponseNotFound(f'Teacher with id={id} does not exists.')
#
#     if request.method == 'POST':
#         form = TeacherEditForm(request.POST, instance=teacher)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('teachers'))
#     else:
#         form = TeacherEditForm(
#             instance=teacher
#         )
#     return render(
#         request=request,
#         template_name='teachers_edit.html',
#         context={'form': form,
#                  'title': 'Edit teachers',
#                  'teacher': teacher, }
#     )
#
#
# def teachers_delete(request, id):
#     Teacher.objects.filter(pk=id).delete()
#     return HttpResponseRedirect(reverse('teachers'))


class TeachersListView(LoginRequiredMixin, ListView):
    model = Teacher
    template_name = 'teachers_list.html'
    context_object_name = 'teachers_list'
    login_url = reverse_lazy('user_account:login')
    paginate_by = 3

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.order_by('-id')
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['title'] = 'Teachers list'
        return context


class TeachersUpdateView(LoginRequiredMixin, UpdateView):
    model = Teacher
    template_name = 'teachers_edit.html'
    form_class = TeacherEditForm
    login_url = reverse_lazy('user_account:login')

    def get_success_url(self):
        return reverse('teachers:list')


class TeachersCreateView(LoginRequiredMixin, CreateView):
    model = Teacher
    template_name = 'teachers_add.html'
    form_class = TeacherAddForm
    login_url = reverse_lazy('user_account:login')

    def get_success_url(self):
        return reverse('teachers:list')


class TeachersDeleteView(LoginRequiredMixin, DeleteView):
    model = Teacher
    template_name = 'teachers_edit.html'
    form_class = TeacherDeleteForm

    def get_success_url(self):
        return reverse('teachers:list')
