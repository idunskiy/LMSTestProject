from django.shortcuts import render

# Create your views here.


def teachers_list(request):
    # return HttpResponse(result)
    return render(
        request=request,
        template_name='teachers.html',
    )
