"""
URL configuration for sanaba project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from sanabaweb import views
from sanabaweb.views import HomeView

urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),  # /i18n/setlang/ pour changer la langue
]

urlpatterns += i18n_patterns(

    path("", HomeView.as_view(), name="home"),
    path("admin/", admin.site.urls),
    path("health", lambda r: HttpResponse("ok")),

    # Services
    path('services/', views.ServicesView.as_view(), name='services'),
    # path('services/data-ia/', views.DataAIView.as_view(), name='data_ai'),
    path('services/cloud-security/', views.CloudSecurityView.as_view(), name='cloud_security'),
    path('services/engineering/', views.EngineeringView.as_view(), name='engineering'),
    path('services/ux-research/', views.UXResearchView.as_view(), name='ux_research'),
    path('services/delivery-management/', views.DeliveryManagementView.as_view(), name='delivery_management'),
    path('services/business-consulting/', views.BusinessConsultingView.as_view(), name='business_consulting'),
    path('services/<slug:slug>/', views.ServiceDetailView.as_view(), name='service_detail'),

    # Insights
    path('insights/', views.InsightsView.as_view(), name='insights'),
    path('insights/<slug:slug>/', views.CaseStudyDetailView.as_view(), name='case_study_detail'),

    # Carrières
    path('careers/', views.CareersView.as_view(), name='careers'),
    path('careers/<slug:slug>/', views.CareerDetailView.as_view(), name='career_detail'),
    path('careers/internship-program/', views.InternshipProgramView.as_view(), name='internship_program'),

    # Contact
    path('contact/', views.ContactView.as_view(), name='contact'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
