from django.urls import path
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('test/', views.testView.as_view()),
    path('validcolumns/', views.validColumns.as_view())
]