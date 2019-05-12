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
    erstWahl = models.ForeignKey(Projekt,on_delete=models.CASCADE,null=True,blank=True,related_name='erstWahl')
    zweitWahl = models.ForeignKey(Projekt,on_delete=models.CASCADE,null=True,blank=True,related_name='zweitWahl')
    drittWahl = models.ForeignKey(Projekt,on_delete=models.CASCADE,null=True,blank=True,related_name='drittWahl')
    klasse = models.CharField(max_length=3)
    def __str__(self):
        return self.name


# Create your models here.
