from django.urls import path, include
from . import views
from .views import homepage, Pesquisa



urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('encontrar_jobs/', views.encontrar_jobs, name="encontrar_jobs"),
    path('aceitar_job/<int:id>/', views.aceitar_job, name="aceitar_job"),
    path('perfil/', views.perfil, name="perfil"),
    path('enviar_projeto/', views.enviar_projeto, name="enviar_projeto"),
    path('pesquisa/', Pesquisa.as_view(), name="pesquisa"),

]