from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Projekt, Schueler

admin.site.register(Projekt)
#admin.site.register(Schueler)

class SchuelerRegister(resources.ModelResource):
    class Meta:
        model = Schueler
        fields = ('id','name', 'klasse', 'erstWahl__name','zweitWahl__name','drittWahl__name',)
        #exclude = ('id', )
        import_id_fields = ('id','name', 'klasse',)

class SchuelerAdmin(ImportExportModelAdmin):
    resource_class = SchuelerRegister

admin.site.register(Schueler, SchuelerAdmin)
# Register your models here.
