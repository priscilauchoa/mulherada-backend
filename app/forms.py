
from django import forms
from sitedemoday.models import Vagas

class BuscarVagas(forms.ModelForm):
    class Meta:
        model = Vagas
        fields = [
            'titulo',
            'cidade'
        ]
