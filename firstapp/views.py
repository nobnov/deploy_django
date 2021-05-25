from django.http import HttpResponse


# Create your views here.
def results(request):
    return HttpResponse('Hello Django App')
