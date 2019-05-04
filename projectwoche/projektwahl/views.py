from django.shortcuts import render
from django.http import HttpResponse
from .models import Projekt, Schueler


def Wahl(request):
    if(request.Type == "POST"):
        try:
            schueler = Schueler.objects.get(name='request.POST.get("name")')
        except Exception as e:
            return render(request, 'projektwahl/projektwahl.html', context={'project': project,
                                                                            'status': "Schüler wurde nicht gefunden"})



    #Standart Site
    project = Projekt.objects.all()
    return render(request, 'projektwahl/projektwahl.html', context={'project': project,
                                                                    'status': ""})
# Create your views here.
