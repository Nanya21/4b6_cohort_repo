from django.urls import path
from .views import test_view, homepage


urlpatterns = [
    path('about/',test_view),
    path('',homepage)
]