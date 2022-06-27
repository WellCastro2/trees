from django import forms
from core.models import PlantedTree


class PlantedCreateForm(forms.ModelForm):
    class Meta:
        model = PlantedTree
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(PlantedCreateForm, self).__init__(*args, **kwargs)
