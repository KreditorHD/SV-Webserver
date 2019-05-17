from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Projekt, Schueler

#admin.site.register(Projekt)
#admin.site.register(Schueler)

class SchuelerRegister(resources.ModelResource):
    class Meta:
        model = Schueler
        fields = ('id','name', 'klasse', 'erstWahl__name','zweitWahl__name','drittWahl__name',)
        #exclude = ('id', )
        import_id_fields = ('id','name', 'klasse',)

class SchuelerAdmin(ImportExportModelAdmin):
    resource_class = SchuelerRegister


# Register your models here.


class ProjektRegister(resources.ModelResource):
    class Meta:
        model = Projekt
        fields = ('id','lehrer', 'name', 'groesse','mitglieder',)
        #exclude = ('id', )
        import_id_fields = ('id','lehrer', 'name', 'groesse','mitglieder',)

class ProjektAdmin(ImportExportModelAdmin):
    resource_class = ProjektRegister


admin.site.register(Schueler, SchuelerAdmin)
admin.site.register(Projekt, ProjektAdmin)
