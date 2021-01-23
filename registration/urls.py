from django.urls import path

from . import views
#from .views import Pdf

urlpatterns = [
    # path("", views.temp),
    path("", views.check, name="check"),
]
