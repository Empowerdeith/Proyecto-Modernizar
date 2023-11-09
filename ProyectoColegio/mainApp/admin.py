from django.contrib import admin
from .models import Reglamento, ToolsLeft, ToolsCenter, ToolsRight
"""from .models import NivTransicion
from .models import EdBasica"""

admin.site.register(Reglamento)
admin.site.register(ToolsLeft)
admin.site.register(ToolsCenter)
admin.site.register(ToolsRight)

"""@admin.register(EdBasica)
class EdBasicaAdmin(admin.ModelAdmin):
    list_display = ('edbasica','utilesCurso')
    ordering = ('edbasica',)
    search_fields =('edbasica',)"""


#admin.site.register(EdBasica,EdBasicaAdmin)