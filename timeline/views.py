from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import MoleculeDisc
 

from .models import *

def timeline(request):

    years = range(1500, 2022)
    return render(request, 'timeline.html', {'years': years})

def year(request, year):
    discoveries = MoleculeDisc.objects.filter(date__year=year)
    return render(request, 'discoveries.html', {'discoveries': discoveries})
