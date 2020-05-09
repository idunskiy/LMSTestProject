from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
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
