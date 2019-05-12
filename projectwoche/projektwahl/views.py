from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Projekt, Schueler


def Wahl(request):
    project = updateProjects()
    students = updateStudents()
    if request.method == "POST":
        try:
            print(request.POST)
            schueler = Schueler.objects.get(name=request.POST.get('student'))
        except Exception:
            return render(request, 'projektwahl/projektwahl.html', context={'project': project,
                                                                            'schueler': students,
                                                                            'status': "Schüler wurde nicht gefunden"})
        print(request.POST.get('project'))
        if request.POST.get('1. Wahl') == 'None' or request.POST.get('2. Wahl') == 'None' or request.POST.get('3. Wahl') == 'None':
            return render(request, 'projektwahl/projektwahl.html', context={'project': project,
                                                                            'schueler': students,
                                                                            'status': "Wahl für {} konnte nicht abgeschlossen werden, da eine Wahl nicht ausgewählt wurde".format(request.POST.get('student'))})
        else:
            eWahl = Projekt.objects.get(name=request.POST.get('1. Wahl'))
            zWahl = Projekt.objects.get(name=request.POST.get('2. Wahl'))
            dWahl = Projekt.objects.get(name=request.POST.get('3. Wahl'))
            schueler.erstWahl = eWahl
            schueler.zweitWahl = zWahl
            schueler.drittWahl = dWahl
            schueler.save()
            project = updateProjects()
            students = updateStudents()

            return render(request, 'projektwahl/projektwahl.html', context={'project': project,
                                                                            'schueler': students,
                                                                            'status': "Wahl für {} abgeschlossen".format(request.POST.get('student'))})

    #Standart Site
    return render(request, 'projektwahl/projektwahl.html', context={'project': project,
                                                                    'schueler': students,
                                                                    'status': ""})

def updateProjects():
    project = []
    for p in Projekt.objects.all():
        project.append(p)
    return project

def updateStudents():
    students = []
    for p in Schueler.objects.all():
        if p.erstWahl != None and p.zweitWahl != None and p.drittWahl != None:
            print('debug')
            continue
        else:
            students.append(p)
    sorted(students, key=lambda students: students.name)
    return students
