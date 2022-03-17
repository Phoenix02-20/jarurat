from django.urls import path
from . import views
from .views import home

urlpatterns = [
    path('', home, name="home"),
    path('contact.html', views.contact, name="contact"),
    path('about-us.html', views.about, name="about-us"),
    path('project.html', views.project, name="project"),
    path('project-details.html', views.project_details, name="project_details"),
    path('service.html', views.service, name="service"),
    path('appointment.html', views.appointment, name="appointment"),
    path('book.html', views.book, name="book"),
]
