from django import forms
from .models import note

class input(forms.ModelForm):
    class Meta:
        model = note
        fields = ['title','text']
        widgets = {'title':forms.TextInput(attrs={'class':'form-control'}),
                    'text':forms.Textarea(attrs={'class':'form-control'})
                   }
        
    def save(self,current_user):
        db_inst = super().save(commit=False)
        db_inst.user = current_user
        return super().save()
    
    
class update_form(forms.ModelForm):
    class Meta:
        model = note
        fields = ['title','text']
        widgets = {'title':forms.TextInput(attrs={'class':'form-control'}),
                    'text':forms.Textarea(attrs={'class':'form-control'})
                   }


