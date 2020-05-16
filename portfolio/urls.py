from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='portfolio_homepage'),
    path('projects/', views.project_page, name='portfolio_project_page'),
    path('contacts/', views.contact_page, name='portfolio_contact_page'),
]