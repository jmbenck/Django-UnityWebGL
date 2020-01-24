"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from rest_framework.authtoken import views
from usuarios.views import usuario_cadastro, ranking, game

from .router import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', game),
    path('login/', LoginView.as_view(template_name="login.html"), name="login"),
    path('logout', LogoutView.as_view(next_page='login'), name="logout"),
    path('autenticar/', views.obtain_auth_token, name='autenticacao-src-token'),
    path('ranking/', ranking, name="ranking"),
    path('cadastro/', usuario_cadastro, name="cadastro"),
    path('api/', include(router.urls)),
    path('game/', game, name="game")
]