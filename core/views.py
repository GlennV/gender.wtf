from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import translation
from django.utils.translation import ugettext_lazy as _
from django.views.generic.base import View
from ipware import get_client_ip

from core.utils import _check_solution_found
from .forms import CaptchaForm, SolutionTryForm
from .models import SolutionTry
from . import config


class KeywordException(BaseException):
    pass


def get_range(count):
    if 1 <= count <= 3:
        return "1-3"

    elif 4 <= count <= 5:
        return "4-5"

    elif 6 <= count <= 7:
        return "6-7"

    elif count == 8:
        return "8"

    return "0"


def about(request):
    return render(request, "general/about.html", {
        "title": _("Welkom")
    })


def verify(request):
    correct_count = 0
    solutions = config.KEYWORD_SOLUTIONS

    captcha_form = CaptchaForm(prefix="captcha")
    form = SolutionTryForm()

    if request.method == "POST":
        try:
            captcha_form = CaptchaForm(request.POST)
            form = SolutionTryForm(request.POST)

            if not captcha_form.is_valid():
                raise KeywordException(_("Invalid reCAPTCHA."))

            if form.is_valid():
                list_guesses = form.cleaned_data.get("keywords")

                for k in solutions:
                    if k in list_guesses:
                        correct_count += 1

                if list_guesses:
                    # Log try
                    SolutionTry.objects.create(
                        keywords=list_guesses,
                        ip=get_client_ip(request)[0],
                        correct_count=correct_count,
                        name=request.POST.get("name")
                    )

                    return render(request, "general/verify.html", {
                        "form": form,
                        "captcha_form": captcha_form,
                        "correct_range": get_range(correct_count),
                        "check_solution_found": _check_solution_found(),
                        "title": _("Solution checker")
                    })

            else:
                raise KeywordException(form.errors["keywords"][0])

        except KeywordException as e:
            messages.error(request, e)

    return render(request, "general/verify.html", {
        "form": form,
        "captcha_form": captcha_form,
        "title": _("Solution checker")
    })


# Add the static pages here (don't make an app for them)
def two(request):
    return render(request, "2/index.html", {
        "title": "Challenge 2"
    })


def four(request):
    return render(request, "4/index.html", {
        "title": "Challenge 4"
    })


def six(request):
    return render(request, "6/index.html", {
        "title": "Challenge 6"
    })


def seven(request):
    return render(request, "7/index.html", {
        "title": "Challenge 7"
    })


def eight(request):
    return render(request, "8/index.html", {
        "title": "Challenge 8"
    })


# Change language view
class ActivateLanguageView(View):
    language_code = ''

    def get(self, request, *args, **kwargs):
        self.language_code = kwargs.get('language_code')
        translation.activate(self.language_code)
        request.session[translation.LANGUAGE_SESSION_KEY] = self.language_code
        return redirect(reverse("about"))
