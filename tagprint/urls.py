
from django.urls import path
from . import views
from .views import NFeListView, GenerateTagView, PrintTagView

urlpatterns = [
    path('nfes/', NFeListView.as_view(), name='nfe_list'),
    path('gerar/<int:nfe_number>/', GenerateTagView.as_view(), name='generate_tag'),
    path('imprimir/<int:nfe_number>/', PrintTagView.as_view(), name='print_tag'),
]
