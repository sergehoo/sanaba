from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html
from .models import Service, Testimonial, Career, CaseStudy


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    # Configuration de l'affichage de la liste
    list_display = ('name', 'display_icon', 'featured', 'order', 'created_at', 'updated_at')
    list_editable = ('featured', 'order')
    list_filter = ('featured', 'created_at', 'updated_at')
    search_fields = ('name', 'short_description', 'full_description')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('order', 'name')

    # Personnalisation de l'affichage de l'icône
    def display_icon(self, obj):
        if obj.icon:
            return format_html('<span style="font-size: 1.5em;">{}</span>', obj.icon)
        return "-"

    display_icon.short_description = _('Icône')

    # Aperçu de l'image
    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 100px; max-width: 100px;" />', obj.image.url)
        return _("Aucune image")

    display_image.short_description = _('Aperçu')

    # Configuration du formulaire d'édition
    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'featured', 'order')
        }),
        (_('Contenu'), {
            'fields': ('short_description', 'full_description')
        }),
        (_('Médias'), {
            'fields': ('icon', 'image', 'display_image'),
            'classes': ('collapse',)
        }),
    )

    readonly_fields = ('created_at', 'updated_at', 'display_image')

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        if obj:  # Si on édite un objet existant
            fieldsets = fieldsets + (
                (_('Métadonnées'), {
                    'fields': ('created_at', 'updated_at'),
                    'classes': ('collapse',)
                }),
            )
        return fieldsets

    # Actions personnalisées
    actions = ['make_featured', 'remove_featured']

    def make_featured(self, request, queryset):
        updated = queryset.update(featured=True)
        self.message_user(request, _('{} services ont été mis en vedette.').format(updated))

    make_featured.short_description = _('Mettre en vedette les services sélectionnés')

    def remove_featured(self, request, queryset):
        updated = queryset.update(featured=False)
        self.message_user(request, _('{} services ont été retirés de la vedette.').format(updated))

    remove_featured.short_description = _('Retirer de la vedette les services sélectionnés')


# CaseStudy Admin
@admin.register(CaseStudy)
class CaseStudyAdmin(admin.ModelAdmin):
    list_display = ('title', 'client', 'featured', 'published_date')
    list_filter = ('featured', 'published_date', 'services')
    search_fields = ('title', 'client', 'content')
    filter_horizontal = ('services',)
    prepopulated_fields = {'slug': ('title',)}

# Testimonial Admin
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'client_company', 'featured')
    list_filter = ('featured',)
    search_fields = ('client_name', 'client_company', 'content')

# Career Admin
@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    list_display = ('title', 'job_type', 'location', 'published')
    list_filter = ('job_type', 'published')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}