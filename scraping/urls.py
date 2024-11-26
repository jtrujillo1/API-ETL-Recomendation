from django.urls import path
from .views import AnalyzeView, MercadoLibreSearchView

urlpatterns = [
    path('search/', MercadoLibreSearchView.as_view(), name='search'),
    path('analyze/', AnalyzeView.as_view(), name='analyze'),
]

