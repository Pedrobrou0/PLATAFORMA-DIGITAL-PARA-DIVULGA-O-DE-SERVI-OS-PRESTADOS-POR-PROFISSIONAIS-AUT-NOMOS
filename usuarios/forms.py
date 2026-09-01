from django import forms
from servicos.models import Categoria
from .models import Profissional


class ProfissionalForm(forms.ModelForm):
    categorias = forms.ModelMultipleChoiceField(
        queryset=Categoria.objects.all(),
        required=True
    )

    class Meta:
        model = Profissional
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'telefone',
            'cidade',
            'descricao',
            'foto',
            'categorias'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance.pk:
            self.fields['categorias'].initial = (
                self.instance.categorias.all()
            )

    def save(self, commit=True):
        profissional = super().save(commit=False)

        if commit:
            profissional.save()

            profissional.categorias.set(
                self.cleaned_data['categorias']
            )

        return profissional