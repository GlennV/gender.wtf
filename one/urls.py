from django.urls import path
from . import views

app_name = 'one'
urlpatterns = [
    path('', views.puzzle, name="puzzle"),
    path('guess/<int:x>/<int:y>/', views.guess, name="guess"),
    path('list-guesses/', views.list_guesses, name="list_guesses"),
]
