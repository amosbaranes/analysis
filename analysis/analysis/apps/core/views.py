from django.shortcuts import render


def index(request):
    title = 'Core App'
    return render(request, 'core/index.html', {'title': title})
