from django.contrib import admin
from .models import Reglamento, ToolsLeft, ToolsCenter, ToolsRight


admin.site.register(Reglamento)


@admin.register(ToolsLeft)
class ToolsLeftAdmin(admin.ModelAdmin):
    list_display = ('nombre','utilesCurso')
    ordering = ('nombre',)
    search_fields =('nombre',)

@admin.register(ToolsRight)
class ToolsRightAdmin(admin.ModelAdmin):
    list_display = ('nombre','utilesCurso')
    ordering = ('nombre',)
    search_fields =('nombre',)
    
    
@admin.register(ToolsCenter)
class ToolsCenterAdmin(admin.ModelAdmin):
    list_display = ('nombre','utilesCurso')
    ordering = ('nombre',)
    search_fields =('nombre',)
