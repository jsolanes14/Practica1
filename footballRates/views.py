from django.shortcuts import render


def user(request):
    return render(request, 'templates/basepage.html')

