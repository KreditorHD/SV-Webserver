from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Projekt, Schueler


def Wahl(request):
    project = project = updateProjects()
    if request.method == "POST":
        try:
            schueler = Schueler.objects.get(name=request.POST.get('name'))
        except Exception:
            return render(request, 'projektwahl/projektwahl.html', context={'project': project,
                                                                            'status': "Schüler wurde nicht gefunden"})
        print(request.POST.get('project'))
        p = Projekt.objects.get(name=request.POST.get('project'))
        if p.mitglieder < p.groesse:
            schueler.projekt.mitglieder = schueler.projekt.mitglieder - 1
            schueler.projekt.save()
            schueler.projekt = p
            schueler.save()
            p.mitglieder = p.mitglieder + 1
            p.save()
            project = updateProjects()
            print(schueler.projekt)
        else:
            return render(request, 'projektwahl/projektwahl.html', context={'project': project,
                                                                            'status': "Projekt ist voll!"})
        return render(request, 'projektwahl/projektwahl.html', context={'project': project,
                                                                        'status': "{} wurde dem Projekt {} zugewiesen".format(request.POST.get('name'),request.POST.get('project'))})

    #Standart Site
    return render(request, 'projektwahl/projektwahl.html', context={'project': project,
                                                                    'status': ""})

def updateProjects():
    project = []
    for p in Projekt.objects.all():
        if p.mitglieder >= p.groesse:
            continue
        else:
            project.append(p)
    return project
