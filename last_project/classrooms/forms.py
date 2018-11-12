from django import forms
from classrooms.models import ClassRoom

class ClassRoomForm(forms.ModelForm):

	class Meta:
		model = ClassRoom
		fields = ('name', 'section', 'description')
		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control'}),
			'section': forms.TextInput(attrs={'class':'form-control'}),
			'description': forms.Textarea(attrs={'class':'form-control'}),
		}
