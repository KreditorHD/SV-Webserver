from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Users

def login(request):
    # zeilen = []
    # for user in Users.objects.all():
    #     zeilen.append('Username: {} Password: {}'.format(user.username,user.password))
    #     zeilen += ['','-' * 30, '']
    # antwort = HttpResponse('\n'.join(zeilen))
    # antwort['Content-Type'] = 'text/plain'
    # return antwort
    #try:
    if request.method == 'POST':
        print(request.POST.get('Username'))
        try:
            user = Users.objects.get(username=request.POST.get('Username'))
        except Exception:
            return render(request, 'login/login.html', context={'username': request.POST.get('Username'),
                                                                   'passwort': '',
                                                                   'status': 'Kein Benutzer mit diesem Namen!'})
        print(type(request.POST.get('Passwort')))
        print("User gefunden!")
        if(user.password == request.POST.get('Passwort')):
            print('Logged in')
            # return render(request, 'login/login.html', context={'username': user.username,
            #                                                     'password': '',
            #                                                     'status': 'Login erfolgreich!'})
            return hackme(request)
        else:
            return render(request, 'login/login.html', context={'username': user.username,
                                                                'password': '',
                                                                'status': 'Login fehlgeschlagen!'})
    else:
        return render(request, 'login/login.html', context={'username': '',
                                                               'passwort': '',
                                                               'status': ''})
def hackme(request):
        zeilen = []
        for user in Users.objects.all():
            zeilen.append('Username: {} Password: {}'.format(user.username,user.password))
            zeilen += ['','-' * 30, '']
        antwort = HttpResponse('\n'.join(zeilen))
        antwort['Content-Type'] = 'text/plain'
        return antwort

# Create your views here.
