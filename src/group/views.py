from django.shortcuts import render

# Create your views here.


def groups_list(request):
    # return HttpResponse(result)
    return render(
        request=request,
        template_name='groups_list.html',
    )
