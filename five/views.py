from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from core.utils import get_ip
from five.forms import GeocacheForm
from five.models import Geocache


def puzzle(request):
    geocaches = Geocache.objects.order_by("order")
    keyword = [' ' for x in range(10)]

    # Compose keyword
    for g in geocaches:
        if g.is_found:
            keyword[(g.order - 1) * 2] = g.solutions[0]
            keyword[(g.order - 1) * 2 + 1] = g.solutions[1]

    return render(request, "5/index.html", {
        "geocaches": geocaches,
        "keyword": ''.join(keyword),
        "title": "Challenge 5"
    })


def found(request, x):
    # Try to get Geocache
    geocache = get_object_or_404(Geocache, guid=x)
    if geocache.is_found:
        print("claimed")
        messages.error(request, _("Whoops, this geocache was already claimed by someone else!"))
        return redirect(reverse("geo:puzzle"))

    # Form
    if request.method == "POST":
        form = GeocacheForm(request.POST)
        if form.is_valid():
            geocache.found_on = timezone.now()
            geocache.name = form.cleaned_data.get("name")
            geocache.ip = get_ip(request)
            geocache.save()

            messages.success(request, _("You succesfully claimed this geocache! "
                                        "Good job, you just unlocked 2 letters of the keyword."))
            return redirect(reverse("geo:puzzle"))

        else:
            messages.error(request, _("Please enter your name!"))

    else:
        form = GeocacheForm()

    return render(request, "5/found.html", {
        "form": form,
        "geocache": geocache,
        "title": "Challenge 5"
    })
