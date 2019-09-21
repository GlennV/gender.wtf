from django import forms


class GeocacheForm(forms.Form):
    name = forms.CharField(initial="Anon")
