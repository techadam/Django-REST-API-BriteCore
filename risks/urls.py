from django.urls import path
from . import views

urlpatterns = [
    path('risks/', views.RiskListView.as_view()),
    path('risks/<int:pk>/', views.RiskDetailView.as_view()),
    path('risk_fields/', views.RiskFieldListView.as_view()),
    path('risk_fields/<int:pk>/', views.RiskFieldDetailView.as_view()),
    path('field_types/', views.FieldTypeListView.as_view())
]