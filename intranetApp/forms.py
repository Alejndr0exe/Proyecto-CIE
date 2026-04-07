from django import forms 
from .models import Categoria, Documento

class addDoc(forms.Form):
    documento = forms.FileField()
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all())
    investigador = forms.CharField(required=False)
    proyecto = forms.CharField(required=False)
    descripcion = forms.CharField(required=False) 
    

class addDoc(forms.ModelForm):
    documento = forms.FileField()
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all())
    investigador = forms.CharField(required=False)
    proyecto = forms.CharField(required=False)
    descripcion = forms.CharField(required=False) 

    class Meta:
        model = Documento
        fields = '__all__'
