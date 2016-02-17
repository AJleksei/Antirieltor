from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return render(request, 'userprofile/index.html', {'test': request.user.first_name })

