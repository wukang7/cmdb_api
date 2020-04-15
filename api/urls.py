from django.urls import path
from api.views import Server
urlpatterns = [
    path(r'server', Server.as_view()),
]