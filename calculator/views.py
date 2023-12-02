from django.http import HttpResponse
from django.shortcuts import render
from .forms import CalculateForm


def home(request):
    return render(request, 'html/home.html')


def result(request):
    try:
        num1 = int(request.GET.get('num1'))
        num2 = int(request.GET.get('num2'))

        if request.GET.get('add') == "":
            ans = num1 + num2

        elif request.GET.get('subtract') == "":
            ans = num1 - num2

        elif request.GET.get('multiply') == "":
            ans = num1 * num2

        else:
            ans = num1 / num2

        return render(request, 'html/result.html', {'ans': ans})
    except:
        return render(request, 'html/error.html')
