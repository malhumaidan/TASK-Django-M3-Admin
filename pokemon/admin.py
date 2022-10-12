from django.contrib import admin
from .models import Pokemon

# Register your models here.

@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ("id","name", "hp", "active",)
    list_display_links = ("id", "name",)
    list_filter = ("active",)
    readonly_fields = ("created_at", "modified_at",)

    fieldsets = (
        (
            "general", {
                "fields": ("name", "hp", "active", "type",)
            }
        ),
        (
            "Localization", {
                "fields": ("name_ar", "name_fr", "name_jp",), "classes": ("collapse",)
            }
        ),
        (
            None, {
                "fields": ("created_at", "modified_at",)
            }
        )
    )

