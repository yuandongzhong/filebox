from django import forms

from .models import TeamFile


class TeamFileForm(forms.ModelForm):
    class Meta:
        model = TeamFile
        fields = ('file', )
