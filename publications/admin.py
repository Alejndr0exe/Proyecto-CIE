from django.contrib import admin
from .models import Publication

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ("autors", "titulo", "fecha", "magazine", "doi", "url")
    list_filter = ("autors", "titulo", "fecha", "magazine")
    search_fields = ("autors", "titulo", "fecha", "magazine")
