from django import forms
from .models import LinksModel
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

def valid_url(to_validate):
    validator = URLValidator()
    try:
        validator(to_validate)
        # url is valid here
        # do something, such as:
        return True
    except:
        return False

class LinkForm(forms.ModelForm):
    class Meta():
        model = LinksModel
        fields = ('cl_link',)
        help_texts = {
            'cl_link': 'The link must start with \"http://\"',
        }
        widgets = {
            'cl_link': forms.TextInput(attrs={'type': 'url'}),
        }

    def __init__(self, *args, **kwargs):
        super(LinkForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def clean_cl_link(self):
        cl_link = self.cleaned_data['cl_link']
        if not valid_url(cl_link):
            raise ValidationError('Link must start with \"http://\"')
        return cl_link