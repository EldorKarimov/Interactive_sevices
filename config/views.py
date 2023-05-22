from django.shortcuts import render
from interactive.models import Leader


def home(request):
    leaders = Leader.objects.all()
    context = {
        'leaders':leaders
    }
    return render(request, 'home.html', context)