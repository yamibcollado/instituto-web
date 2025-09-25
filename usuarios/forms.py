from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class RegistroForm(UserCreationForm):
    documento = forms.IntegerField(
        required=True,
        label="Documento",
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Ingresá tu documento"})
    )
    nombre = forms.CharField(
        required=True,
        label="Nombre",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingresá tu nombre"})
    )
    apellido = forms.CharField(
        required=True,
        label="Apellido",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingresá tu apellido"})
    )
    telefono = forms.CharField(
        required=False,
        label="Teléfono",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Opcional"})
    )

    class Meta:
        model = Usuario
        fields = ["documento", "nombre", "apellido", "telefono", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Aplicar clases Bootstrap a los campos de contraseña
        self.fields["password1"].label = "Contraseña"
        self.fields["password1"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Ingresá tu contraseña"
        })
        self.fields["password2"].label = "Confirmar contraseña"
        self.fields["password2"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Repetí tu contraseña"
        })
