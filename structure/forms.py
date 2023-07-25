from django import forms
from .models import Equipe

# class NotationWidget(forms.TextInput):
#     def format_value(self, value):
#         if value is not None:
#             return "{:.2f}".format(value)
#         return ""




# class ActiviteForm(forms.ModelForm):
#     class Meta:
#         model = Activite
#         fields = '__all__'
#         widgets = {
#             'notation': NotationWidget(),
#         }

class EquipeFiltreForm(forms.Form):
    recherche = forms.CharField(required=False)
    respo = forms.ChoiceField(choices=[], required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        responsables = set()
        for equipe in Equipe.objects.all():
            if equipe.respo:
                responsables.add((equipe.respo.id, equipe.respo.nom))
        self.fields['respo'].choices = [('', '--------')] + sorted(responsables, key=lambda x: x[1])


