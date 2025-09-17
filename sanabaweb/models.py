from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
from django.urls import reverse


# Create your models here.
class FeaturedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(featured=True)


class CaseStudyManager(models.Manager):
    def featured(self):
        return self.get_queryset().filter(featured=True)


class TestimonialManager(models.Manager):
    def featured(self):
        return self.get_queryset().filter(featured=True)


class ServiceManager(models.Manager):
    def featured(self):
        return self.get_queryset().filter(featured=True)


class Service(models.Model):
    name = models.CharField(_("Nom"), max_length=200)
    slug = models.SlugField(_("Slug"), unique=True)
    short_description = models.TextField(_("Description courte"))
    full_description = RichTextField(_("Description complète"))
    icon = models.CharField(_("Icône"), max_length=50, blank=True)
    image = models.ImageField(_("Image"), upload_to='services/', blank=True, null=True)
    featured = models.BooleanField(_("En vedette"), default=False)
    order = models.PositiveIntegerField(_("Ordre"), default=0)
    created_at = models.DateTimeField(_("Date de création"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Date de modification"), auto_now=True)

    objects = models.Manager()  # Manager par défaut
    featured_objects = ServiceManager()  # Manager pour les éléments en vedette

    class Meta:
        verbose_name = _("Service")
        verbose_name_plural = _("Services")
        ordering = ['order', 'name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('service_detail', kwargs={'slug': self.slug})


class CaseStudy(models.Model):
    title = models.CharField(_("Titre"), max_length=200)
    slug = models.SlugField(_("Slug"), unique=True)
    excerpt = models.TextField(_("Extrait"))
    content = models.TextField(_("Contenu"))
    client = models.CharField(_("Client"), max_length=200)
    industry = models.CharField(_("Secteur"), max_length=100)
    challenge = models.TextField(_("Défi"))
    solution = models.TextField(_("Solution"))
    results = models.TextField(_("Résultats"))
    image = models.ImageField(_("Image"), upload_to='case_studies/', blank=True, null=True)
    featured = models.BooleanField(_("En vedette"), default=False)
    published_date = models.DateField(_("Date de publication"))
    services = models.ManyToManyField(Service, verbose_name=_("Services associés"), blank=True)

    objects = models.Manager()  # Manager par défaut
    featured_objects = CaseStudyManager()  # Manager pour les études en vedette

    class Meta:
        verbose_name = _("Étude de cas")
        verbose_name_plural = _("Études de cas")
        ordering = ['-published_date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('case_study_detail', kwargs={'slug': self.slug})


class Testimonial(models.Model):
    client_name = models.CharField(_("Nom du client"), max_length=200)
    client_position = models.CharField(_("Poste"), max_length=200)
    client_company = models.CharField(_("Entreprise"), max_length=200)
    content = models.TextField(_("Témoignage"))
    image = models.ImageField(_("Photo"), upload_to='testimonials/', blank=True, null=True)
    featured = models.BooleanField(_("En vedette"), default=False)

    objects = models.Manager()  # Manager par défaut
    featured_objects = TestimonialManager()  # Manager pour les témoignages en vedette

    class Meta:
        verbose_name = _("Témoignage")
        verbose_name_plural = _("Témoignages")
        ordering = ['client_name']

    def __str__(self):
        return f"{self.client_name} - {self.client_company}"


class Career(models.Model):
    JOB_TYPES = [
        ('full_time', _("Temps plein")),
        ('part_time', _("Temps partiel")),
        ('contract', _("Contrat")),
        ('internship', _("Stage")),
    ]

    title = models.CharField(_("Titre du poste"), max_length=200)
    slug = models.SlugField(_("Slug"), unique=True)
    description = models.TextField(_("Description"))
    requirements = models.TextField(_("Exigences"))
    benefits = models.TextField(_("Avantages"))
    job_type = models.CharField(_("Type d'emploi"), max_length=20, choices=JOB_TYPES)
    location = models.CharField(_("Lieu"), max_length=100)
    published = models.BooleanField(_("Publié"), default=True)
    created_at = models.DateTimeField(_("Date de création"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Date de modification"), auto_now=True)

    class Meta:
        verbose_name = _("Carrière")
        verbose_name_plural = _("Carrières")
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('career_detail', kwargs={'slug': self.slug})
