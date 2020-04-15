"""drf URL Configuration

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
from django.urls import path, include, re_path
from drf import view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include("api.urls")),

    # path('depart/$',view.Depart.as_view()),
    # re_path('depart/$', view.DepartView.as_view()),
    # re_path('depart/(?P<pk>\d)/$', view.DepartView.as_view()),

    re_path('newdepart/$', view.NewDepartView.as_view({'get': 'list','post':'create'})),
    re_path('newdepart/(?P<pk>\d)/$', view.NewDepartView.as_view({'get':'retrieve','delete':'destroy','put':'update','patch':'partial_update'}))
]
