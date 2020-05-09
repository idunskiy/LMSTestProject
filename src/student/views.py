from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from student.forms import StudentAddForm
from student.models import Student


def generate_student(request):
    number = request.GET.get('number', 10)
    if number is not None:
        for i in range(int(number)):
            Student.generate_student()
        return HttpResponse(f'"{number}" of students were generated.')


def student_list(request):
    qs = Student.objects.all()

    if request.GET.get('fname'):
        qs = qs.filter(first_name = request.GET.get('fname'))

    if request.GET.get('lname'):
        qs = qs.filter(last_name=request.GET.get('lname'))

    result = '<br>'.join(
        str(student)
        for student in qs
    )
    # return HttpResponse(result)
    return render(
        request=request,
        template_name='students_list.html',
        context={'students_list': result}
    )


def students_add(request):

    if request.method == 'POST':
        form = StudentAddForm()
    else:
        form = StudentAddForm()
    return render(
        request=request,
        template_name='students_add.html',
        context={'form': form}
    )
