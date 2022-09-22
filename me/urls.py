from django.urls import path
from me.views import AboutView


urlpatterns = [
    path('', AboutView.as_view()),
]