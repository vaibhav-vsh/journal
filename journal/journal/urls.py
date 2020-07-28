"""journal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from journal_app import views
from django.conf.urls import include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(),name='home'),
    path('signup',views.SignupView.as_view(),name='signup'),
    path('login',views.LoginUserView.as_view(),name='login'),
    path('logout',auth_views.LogoutView.as_view(),name='logout'),
    path('create',views.create_entry,name='create'),
    path('list',views.EntryList.as_view(),name='list'),
    path('about',views.AboutView.as_view(),name='about'),
    path('edit/<int:pk>',views.EntryEdit.as_view(),name='edit'),
    path('delete/<int:pk>',views.DeleteEntry.as_view(),name='delete')
]
