from django.http import HttpResponse


def index(request):
    print(request)
    return HttpResponse('<h1>Todo Dashboard (Stub)</h1>')
