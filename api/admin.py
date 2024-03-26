from django.contrib import admin
from django.utils.html import format_html
from . import models


class CountryImageInline(admin.TabularInline):
    model = models.CountryImage
    fields = ["image"]


@admin.register(models.Costumer)
class CountryAdmin(admin.ModelAdmin):
    list_display = ["user", "bio", "cover_photo"]


@admin.register(models.CountryImage)
class CountryImageAdmin(admin.ModelAdmin):
    list_display = ["id", "country", "image"]
    search_fields = ["country__name"]
    list_filter = ["country__continent"]


@admin.register(models.Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "capital", "continent", "display_flag_image"]
    search_fields = ["name", "capital"]
    list_filter = ["continent"]
    inlines = [CountryImageInline]

    def display_flag_image(self, obj):
        return format_html(
            '<img src="{}" style="max-width:40px; max-height:40px;" />', obj.flag_url
        )

    display_flag_image.short_description = "Flag"


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "country", "rating", "created_at")
    list_filter = ("country", "rating", "created_at")
    search_fields = ("user__username", "country__name", "rating", "comment")
    readonly_fields = ("created_at",)


@admin.register(models.Visa)
class VisaAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "country",
    )
    list_filter = ("country",)
    search_fields = ["title", "country__name"]


@admin.register(models.ActivityCategory)
class ActivityCategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(models.ActivityImage)
class ActivityImageAdmin(admin.ModelAdmin):
    list_display = ["activity", "image"]


class ActivityImageInline(admin.TabularInline):
    model = models.ActivityImage
    extra = 1


@admin.register(models.Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "country"]
    inlines = [ActivityImageInline]
