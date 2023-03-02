"""tundra URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin, sitemaps
from django.urls import path
from index import views
from personal_account import views_lk


urlpatterns = [
    path('robots.txt', views.RobotsTxtView.as_view()),
    path('sitemap.xml', views.SitemapXmlView.as_view()),
    path('', views.index, name='index'),
    path('lk/', views_lk.index_lk, name='lk'),
    path('lk/<course_id>', views_lk.course_themes, name='course'),
    path('lk/<course_id>/<theme_id>', views_lk.theme_tasks, name='theme'),
    path('login/', views.login_user, name='login'),
    path('admin/', admin.site.urls),
    path('logout_user', views_lk.logout_user, name='logout')
]

handler404 = "index.views.page_not_found_view"
