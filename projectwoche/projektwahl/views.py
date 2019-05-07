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
        p = Projekt.objects.get(name=request.POST.get('project'))
        if p.mitglieder < p.groesse:
            schueler.projekt = p
            schueler.save()
            p.mitglieder = p.mitglieder + 1
            p.save()
            project = updateProjects()
            students = updateStudents()
            print(schueler.projekt)
        else:
            return render(request, 'projektwahl/projektwahl.html', context={'project': project,
                                                                            'schueler': students,
                                                                            'status': "Projekt ist voll!"})
        return render(request, 'projektwahl/projektwahl.html', context={'project': project,
                                                                        'schueler': students,
                                                                        'status': "{} wurde dem Projekt {} zugewiesen".format(request.POST.get('student'),request.POST.get('project'))})

    #Standart Site
    return render(request, 'projektwahl/projektwahl.html', context={'project': project,
                                                                    'schueler': students,
                                                                    'status': ""})

def updateProjects():
    project = []
    for p in Projekt.objects.all():
        if p.mitglieder >= p.groesse:
            continue
        else:
            project.append(p)
    return project

def updateStudents():
    students = []
    for p in Schueler.objects.all():
        print(p.projekt)
        if p.projekt != None:
            print('debug')
            continue
        else:
            students.append(p)
    sorted(students, key=lambda students: students.name)
    return students
