from django.urls import path

import jobs
from . import views
from django.contrib.auth import views as auth_view



urlpatterns = [
    path('cadastro/', views.cadastro, name="cadastro" ),
    path('logar/', views.logar, name="logar"),
    path('sair/', views.sair, name="sair"),
    path('password_reset/', auth_view.PasswordResetView.as_view(template_name="password_reset.html"), name="password_reset"),
    path('password_reset_done/', auth_view.PasswordResetDoneView.as_view(template_name="password_reset_done.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name="password_reset_confirm_view.html"), name="password_reset_confirm"),
    path('password_reset_complete/', auth_view.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"), name="password_reset_complete"),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name='logout'),

]
