from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include

from core.views import ActivateLanguageView
from three import views as views_three
from core import views as views_about

urlpatterns = i18n_patterns(
    path('', views_about.about, name="about"),
    path('verify/', views_about.verify, name="verify"),

    path('1/', include('one.urls', namespace="one")),

    path('2/', views_about.two, name="two"),

    path('3/', views_three.sounds, name="three"),
    path('thr33/', views_three.images),
    path('<3/', views_three.video),

    path('4/', views_about.four, name="four"),

    path('5/', include('five.urls', namespace="five")),
    path('geo/', include('five.urls', namespace="geo")),

    path('6/', views_about.six, name="six"),

    path('7/', views_about.seven, name="seven"),

    path('8/', views_about.eight, name="eight"),
)

urlpatterns += [
    path('lang/<language_code>/', ActivateLanguageView.as_view(), name='language'),
]