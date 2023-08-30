from django.http import HttpResponse


def index(request):
    """Example view function

    Args:
        request (_type_): The example request object

    Returns:
        _type_: The example response object
    """
    print(request)
    return HttpResponse('<h1>Todo Dashboard (Stub)</h1>')
