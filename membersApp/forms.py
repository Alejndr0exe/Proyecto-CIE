from django import forms 
from .models import Members

class addMember(forms.ModelForm):
	class Meta:
		model = Members
		fields = ('nombre','titulo','academic_rank','email','g_scholar','img','descripcion')
