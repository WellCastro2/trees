"""trees URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include


from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),

    path('', views.Home.as_view(), name="home"),
    path('planted-tree/<uuid:pk>/', views.DetailTree.as_view(), name='planted-detail'),
    path('planted-tree/account/<uuid:pk>/', views.ListAccountTree.as_view(), name='planted-list'),
    path('planted-tree/add/', views.PlantTreeView.as_view(), name='planted-add'),
    path('planted-tree/api/list', views.JsonView.as_view(), name='json-tree'),
]

admin.site.site_header = "Trees Everywhere Admin"
admin.site.site_title = "Trees Everywhere Admin Portal"
admin.site.index_title = "Welcome to Trees Everywhere"
