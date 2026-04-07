from django.contrib import admin
from .models import Categoria, Documento

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("nombre",)

@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = ("id", "documento", "categoria", "investigador", "proyecto", "created_at", "updated")
    list_filter = ("categoria", "investigador", "proyecto", "created_at")
    search_fields = ("documento", "descripcion", "investigador", "proyecto")
    date_hierarchy = "created_at"
