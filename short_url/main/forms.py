from django import forms
from .models import LinksModel

class LinkForm(forms.ModelForm):
    class Meta():
        model = LinksModel
        fields = ('cl_link',)
        help_texts = {
            'cl_link': 'We do not store information about you',
        }

    def __init__(self, *args, **kwargs):
        super(LinkForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'