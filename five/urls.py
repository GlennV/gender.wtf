from django.urls import path
from . import views

app_name = 'five'
urlpatterns = [
    path('', views.puzzle, name="puzzle"),
    path('<uuid:x>', views.found, name="found"),
]
