from django.db import models

class Projekt(models.Model):
    lehrer = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    groesse = models.IntegerField();
    mitglieder = models.IntegerField(default=0);

    def __str__(self):
        return self.name

class Schueler(models.Model):
    name = models.CharField(max_length=100)
    projekt = models.ForeignKey(Projekt,on_delete=models.CASCADE,null=True,blank=True)
    klasse = models.CharField(max_length=3)
    def __str__(self):
        return self.name


# Create your models here.
