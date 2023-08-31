from django.shortcuts import render
from calendar_api import test_calendar


def demo(request):
    results = test_calendar()
    context = {"results": results}
    return render(request, 'demo.html', context)
