from django.urls import path
from creativetask.me.views import AboutView


urlpatterns = [
    path("", AboutView.as_view()),
]
