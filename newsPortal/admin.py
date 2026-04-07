from django.contrib import admin
from .models import Noticias, Parrafos, Imgs, Videos


class ParrafosInline(admin.TabularInline):
    model = Parrafos
    extra = 1
    fields = ("subtitulo", "cuerpo")
    show_change_link = True


class ImgsInline(admin.TabularInline):
    model = Imgs
    extra = 1
    fields = ("descricion", "img")
    show_change_link = True


class VideosInline(admin.TabularInline):
    model = Videos
    extra = 1
    fields = ("descricion", "video")
    show_change_link = True


@admin.register(Noticias)
class NoticiasAdmin(admin.ModelAdmin):
    list_display = ("id", "encabezado", "fecha", "parrafos_count", "imgs_count", "videos_count")
    list_filter  = ("fecha",)
    search_fields = ("encabezado", "bajada")
    date_hierarchy = "fecha"
    inlines = [ParrafosInline, ImgsInline, VideosInline]

    def parrafos_count(self, obj):
        return obj.parrafos.count()
    parrafos_count.short_description = "Párrafos"

    def imgs_count(self, obj):
        return obj.imgs.count()
    imgs_count.short_description = "Imágenes"

    def videos_count(self, obj):
        return obj.videos.count()
    videos_count.short_description = "Videos"


@admin.register(Parrafos)
class ParrafosAdmin(admin.ModelAdmin):
    list_display = ("id", "subtitulo", "noticia")
    search_fields = ("subtitulo", "cuerpo")
    autocomplete_fields = ("noticia",)


@admin.register(Imgs)
class ImgsAdmin(admin.ModelAdmin):
    list_display = ("id", "descricion", "noticia")
    search_fields = ("descricion",)
    autocomplete_fields = ("noticia",)


@admin.register(Videos)
class VideosAdmin(admin.ModelAdmin):
    list_display = ("id", "descricion", "noticia")
    search_fields = ("descricion",)
    autocomplete_fields = ("noticia",)
