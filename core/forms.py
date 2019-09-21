from captcha.fields import ReCaptchaField
from django import forms
from django.utils.text import Truncator
from django.utils.translation import ugettext_lazy as _


class CaptchaForm(forms.Form):
    captcha = ReCaptchaField()


class SolutionTryForm(forms.Form):
    name = forms.CharField(initial="Anon")
    keywords = forms.CharField(widget=forms.Textarea(attrs={
        "placeholder": "keywordone,keywordtwo"
    }), required=False)

    def clean_keywords(self):
        keywords = self.cleaned_data.get("keywords")

        # Newlines to comma
        keywords = keywords.replace(" ", "").replace("\r\n", ",")

        # Split by comma & filter out empty guesses
        list_guesses = [x for x in keywords.replace(" ", "").split(",") if x]

        if not list_guesses:
            self.add_error("keywords", _("Please enter between 1 and 8 keywords."))

        elif len(list_guesses) > 8:
            self.add_error("keywords", _("Please enter at most 8 keywords."))

        else:
            for g in list_guesses:
                if not (g.isalpha() and len(g) == 10):
                    self.add_error("keywords", _("Invalid keyword \"%(keyword)s\". "
                                                 "Keywords are letters only and exactly 10 characters long.") % {
                        "keyword": Truncator(g).chars(20)
                    })

        return keywords.lower()
