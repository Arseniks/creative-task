from django.urls import path
from polls.views import AboutView


urlpatterns = [
    path('', AboutView.as_view()),
]