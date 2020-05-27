import json

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound

# Create your views here.
from django.urls import reverse
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from student.forms import StudentAddForm, StudentEditForm, StudentDeleteForm
from student.models import Student


def generate_student(request):
    number = request.GET.get('number', 10)
    if number is not None:
        for i in range(int(number)):
            Student.generate_student()
        return HttpResponse(f'"{number}" of students were generated.')


def student_list(request):
    qs = Student.objects.all().select_related('group')

    # AND filter implementation

    # if request.GET.get('fname'):
    # qs.filter(first_name = request.GET.get('fname'))
    #
    # if request.GET.get('lname'):
    #     qs = Q(question__startswith=request.GET.get('lname'))
    #     # qs = qs.filter(last_name=request.GET.get('lname'))
    #
    # if request.GET.get('email'):
    #     qs = qs.filter(email=request.GET.get('email'))

    # OR filter implementation
    if request.GET.get('fname') or request.GET.get('lname') or request.GET.get('email'):
        query = (Q(first_name=request.GET.get('fname')) |
                  Q(last_name=request.GET.get('lname')) |
                   Q(email=request.GET.get('email')))
        qs = qs.filter(query)

    return render(
        request=request,
        template_name='students_list.html',
        context={'students_list': qs,
                 'title': 'Students list'}
    )


def students_add(request):
    if request.method == 'POST':
        form = StudentAddForm(request.POST)
        if form.is_valid():
            qs = Student.objects.all()
            query = (Q(email=form.cleaned_data['email']) | Q(phone_number=form.cleaned_data['phone_number']))
            qs = qs.filter(query)
            if not qs.exists():
                print(qs)
                form.save()
                return HttpResponseRedirect(reverse('students:list'))
            else:
                qs = qs.first()
                print(f"{qs.email} + {qs.phone_number}")
                response = HttpResponse(f'Student with email: {qs.email} or with '
                                    f'phone: {qs.phone_number} already exists')
                response.status_code = 409
                return response
    else:
        form = StudentAddForm()
    return render(
        request=request,
        template_name='students_add.html',
        context={'form': form,
                 'title': 'Add students'}
    )


def students_edit(request, id):
    try:
        student = Student.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f'Student with id={id} does not exists.')

    if request.method == 'POST':
        form = StudentEditForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students:list'))
    else:
        form = StudentEditForm(
            instance=student
        )
    return render(
        request=request,
        template_name='students_edit.html',
        context={'form': form,
                 'title': 'Edit students',
                 'student': student, }
    )


def students_delete(request, id):
    Student.objects.filter(pk=id).delete()
    return HttpResponseRedirect(reverse('students:list'))


class StudentsListView(ListView):
    model = Student
    template_name = 'students_list.html'
    context_object_name = 'students_list'

    def get_queryset(self):
        qs = super().get_queryset().select_related('group')
        qs = qs.order_by('-id')
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['title'] = 'Students list'
        return context


class StudentsUpdateView(UpdateView):
    model = Student
    template_name = 'students_edit.html'
    form_class = StudentEditForm

    def get_success_url(self):
        return reverse('students:list')


class StudentsCreateView(CreateView):
    model = Student
    template_name = 'students_add.html'
    form_class = StudentAddForm

    def get_success_url(self):
        return reverse('students:list')


class StudentsDeleteView(DeleteView):
    model = Student
    template_name = 'students_edit.html'
    form_class = StudentDeleteForm

    def get_success_url(self):
        return reverse('students:list')
