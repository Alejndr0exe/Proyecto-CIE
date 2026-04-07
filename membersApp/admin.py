from django.contrib import admin
from django.utils.html import format_html
from .models import Area, Members


# ---------- Inlines ----------
class MembersInline(admin.TabularInline):
    model = Members
    extra = 1
    fields = ("nombre", "titulo", "email", "puesto", "mini_foto")
    readonly_fields = ("mini_foto",)

    def mini_foto(self, obj):
        if obj and obj.img:
            return format_html(
                '<img src="{}" style="height:48px;border-radius:6px;" />',
                obj.img.url
            )
        return "—"
    mini_foto.short_description = "Foto"


# ---------- Area ----------
@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nombre",
        "miembros_count",   # definido PRIMERO
        "mini_icono",       # luego icono
        "responsable",
    )
    search_fields = ("nombre", "descripcion", "fragmento")
    inlines = [MembersInline]
    ordering = ("nombre",)
    list_select_related = ("responsable",)

    # 1. Método para contar miembros (VA PRIMERO en list_display)
    def miembros_count(self, obj):
        return obj.miembros.count()
    miembros_count.short_description = "Miembros"

    # 2. Thumbnail pequeño del icono en lista
    def mini_icono(self, obj):
        if obj.icono:
            return format_html(
                '<img src="{}" style="width:24px;height:24px;" />',
                obj.icono.url
            )
        return "—"
    mini_icono.short_description = "Icono"

    # Fieldsets organizados
    fieldsets = (
        ("📋 Info Principal", {
            "fields": ("nombre", "icono", "preview_icono")
        }),
        ("📝 Contenido", {
            "fields": ("fragmento", "descripcion")
        }),
        ("👤 Responsable", {
            "fields": ("responsable",)
        }),
        ("🖼️ Imágenes", {
            "fields": ("portada", "preview_portada")
        }),
    )
    readonly_fields = ("preview_icono", "preview_portada")

    # Previews grandes
    def preview_icono(self, obj):
        if obj.icono:
            return format_html(
                '<img src="{}" style="width:48px;height:48px;border-radius:4px;" />',
                obj.icono.url
            )
        return "Sin icono"
    preview_icono.short_description = "Vista previa icono"

    def preview_portada(self, obj):
        if obj.portada:
            return format_html(
                '<img src="{}" style="max-height:200px;border-radius:8px;" />',
                obj.portada.url
            )
        return "Sin portada"
    preview_portada.short_description = "Vista previa portada"


# ---------- Members ----------
@admin.register(Members)
class MembersAdmin(admin.ModelAdmin):
    list_display = (
        "mini_foto",
        "nombre",
        "titulo",
        "academic_rank",
        "email",
        "universidad",
        "puesto",
        "area",
    )
    list_filter = ("area", "universidad", "puesto", "academic_rank")
    search_fields = ("nombre", "email", "titulo", "universidad", "puesto", "g_scholar")
    autocomplete_fields = ("area",)
    list_select_related = ("area",)
    ordering = ("nombre",)

    readonly_fields = ("preview_foto",)
    fieldsets = (
        ("👤 Identificación", {
            "fields": ("nombre", "area", "titulo", "academic_rank", "puesto", "universidad")
        }),
        ("📧 Contacto", {
            "fields": ("email", "g_scholar")
        }),
        ("🖼️ Imagen", {
            "fields": ("img", "preview_foto")
        }),
        ("📄 Descripción", {
            "fields": ("descripcion",)
        }),
    )

    # Thumbnail en listado
    def mini_foto(self, obj):
        if obj.img:
            return format_html(
                '<img src="{}" style="height:38px;border-radius:6px;" />',
                obj.img.url
            )
        return "—"
    mini_foto.short_description = "Foto"

    # Vista previa grande
    def preview_foto(self, obj):
        if obj and obj.img:
            return format_html(
                '<img src="{}" style="max-height:180px;border-radius:10px;" />',
                obj.img.url
            )
        return "Sin imagen"
    preview_foto.short_description = "Vista previa"
