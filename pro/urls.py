"""pro URL Configuration

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
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', views.form1, name="form1"),
    path('', views.form2, name="form2"),
    path('resp/', views.resp, name="resp"),
    path('create_topic/', views.add_topic, name="create_topic"),
    path("create_webpage/", views.create_webpage, name="create_webpage"),
    path("add_webpage/", views.add_webpage, name="add_webpage"),
    path("uptop/<id>", views.update_topic, name="update_topic"),
    path("upweb/<id>", views.update_webpage, name="update_webpage"),
    path("imgupld/", views.imgupld, name="imgupld")

]

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
