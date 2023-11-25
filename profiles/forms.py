from django import forms
from .models import Profile

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image','description']

class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image','description']

        labels = {
            'image': 'Subir Foto de Perfil',  # Cambia la etiqueta del campo 'image'
            'description': 'Danos una breve descripción de ti!',  # Cambia la etiqueta del campo 'description'
        }

        help_texts = {
           'image': "",
           'description': ""
        }

        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),  # Ajusta el número de filas según tus necesidades
            'image': forms.FileInput()
        }

    def as_table(self):
        return self._html_output(
            normal_row='<tr%(html_class_attr)s><th>%(label)s</th><td>%(field)s%(help_text)s</td></tr>',
            error_row='<tr><td colspan="2">%s</td></tr>',
            row_ender='</td></tr>',
            help_text_html=' <br><span class="helptext">%s</span>',
            errors_on_separate_row=True,
        )       