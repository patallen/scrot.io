from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit


class UrlScrotForm(forms.Form):
    url = forms.CharField(required=True)

    def __init__(self, *args, **kwargs):
        super(UrlScrotForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Div("url", css_class="col-lg-10"),
            Submit('submit', 'Scrot It', css_class="col-lg-2")
        )
