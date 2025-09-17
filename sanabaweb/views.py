from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView

from sanabaweb.models import Service, Testimonial, CaseStudy, Career


# Create your views here.


# Vue d'accueil
class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.all()[:6]
        context['testimonials'] = Testimonial.objects.all()[:2]
        context['case_studies'] = CaseStudy.objects.all()[:3]
        return context


# Vues pour les services
# Vues pour les services
class ServicesView(ListView):
    model = Service
    template_name = 'services/services.html'
    context_object_name = 'services'


class ServiceDetailView(DetailView):
    model = Service
    template_name = 'services/service_detail.html'
    context_object_name = 'service'


# Vues pour Data & IA
# class DataAIView(TemplateView):
#     template_name = 'services/data_ai.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # Ajoutez des données spécifiques si nécessaire
#         return context


class InsightsView(ListView):
    model = CaseStudy
    template_name = 'insights/insights.html'
    context_object_name = 'case_studies'
    paginate_by = 6
    ordering = ['-published_date']


class CaseStudyDetailView(DetailView):
    model = CaseStudy
    template_name = 'insights/case_study_detail.html'
    context_object_name = 'case_study'


# Vues pour Carrières
class CareersView(ListView):
    model = Career
    template_name = 'careers/careers.html'
    context_object_name = 'careers'
    queryset = Career.objects.filter(published=True)


class CareerDetailView(DetailView):
    model = Career
    template_name = 'careers/career_detail.html'
    context_object_name = 'career'

    def get_queryset(self):
        return Career.objects.filter(published=True)


class InternshipProgramView(TemplateView):
    template_name = 'careers/internship_program.html'


# Vue de contact
class ContactView(TemplateView):
    template_name = 'contact/contact.html'


# Vues pour Cloud & Sécurité
class CloudSecurityView(TemplateView):
    template_name = 'services/cloud_security.html'


# Vues pour Ingénierie Logicielle
class EngineeringView(TemplateView):
    template_name = 'services/engineering.html'


# Vues pour UX & Recherche
class UXResearchView(TemplateView):
    template_name = 'services/ux_research.html'


# Vues pour Delivery Management
class DeliveryManagementView(TemplateView):
    template_name = 'services/delivery_management.html'


# Vues pour Conseil Métier
class BusinessConsultingView(TemplateView):
    template_name = 'services/business_consulting.html'


# Vues pour Insights/Études de cas
class InsightsView(ListView):
    model = CaseStudy
    template_name = 'insights/insights.html'
    context_object_name = 'case_studies'
    paginate_by = 6


class CaseStudyDetailView(DetailView):
    model = CaseStudy
    template_name = 'insights/case_study_detail.html'
    context_object_name = 'case_study'


# Vues pour Carrières
class CareersView(ListView):
    model = Career
    template_name = 'careers/careers.html'
    context_object_name = 'careers'


class CareerDetailView(DetailView):
    model = Career
    template_name = 'careers/career_detail.html'
    context_object_name = 'career'


class InternshipProgramView(TemplateView):
    template_name = 'careers/internship_program.html'


# Vue de contact
class ContactView(TemplateView):
    template_name = 'contact/contact.html'

    def post(self, request, *args, **kwargs):
        # Logique pour traiter le formulaire de contact
        # (à implémenter selon vos besoins)
        return render(request, self.template_name, self.get_context_data())
