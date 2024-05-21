from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import MoleculeDisc
 

from .models import *

def timeline(request):

    years = range(1500, 2025)
    return render(request, 'timeline.html', {'years': years})

def year(request, year):
    d = MoleculeDisc.objects.filter(date__year=year).values('description')
    print((d))
    listd = list(d)
    descriptions = [entry['description'] for entry in listd]
    print(descriptions)
    discoveries= ', '.join(descriptions)
    print(discoveries)
    print(f"Year: {year}, Discoveries: {discoveries}")
    return HttpResponse(discoveries, content_type="text/plain")

