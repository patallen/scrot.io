from django import forms


class UrlScrotForm(forms.Form):
    url = forms.CharField(required=True)
