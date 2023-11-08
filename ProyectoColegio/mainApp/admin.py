from django.contrib import admin
from .models import Reglamento
from .models import NivTransicion
from .models import EdBasica

admin.site.register(Reglamento)
admin.site.register(NivTransicion)
#admin.site.register(EdBasica)

@admin.register(EdBasica)
class EdBasicaAdmin(admin.ModelAdmin):
    list_display = ('edbasica','utilesCurso')
    ordering = ('edbasica',)
    search_fields =('edbasica',)


#admin.site.register(EdBasica,EdBasicaAdmin)