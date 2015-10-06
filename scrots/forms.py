from django import forms
from crispy_forms.helper import FormHelper


class UrlScrotForm(forms.Form):
    url = forms.CharField(required=True)

    def __init__ (self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        super(UrlScrotForm, self).__init__(*args, **kwargs)
