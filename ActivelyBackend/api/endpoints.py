from django.urls import path

from .engine.database import Fake_Database
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('test/', views.test_view.as_view()),
    path('validcolumns/', views.valid_columns.as_view()),
    path('trainmodel/', views.train_model.as_view()),
    path('inference/', views.inference.as_view())
]

# declare the instnce of our pseudo db on applicaiton start
global_database_instance = Fake_Database()