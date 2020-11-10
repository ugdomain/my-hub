from django import forms
from .models import DataForm

class formdata(forms.ModelForm):
    class Meta:
        model=DataForm
        fields=['id','Date','Sizeofcontainer','From','To','Customer','Carriedby','Diesel','Price','Status']
        labels={
            'Sizeofcontainer':'Size Of Container',
            'Carriedby':'Carried By',
        }
        widgets={
            'Date':forms.DateInput(attrs={'class':'form-control'}),
            'Sizeofcontainer':forms.TextInput(attrs={'class':'form-control'}),
            'From':forms.TextInput(attrs={'class':'form-control'}),
            'To':forms.TextInput(attrs={'class':'form-control'}),
            'Customer':forms.TextInput(attrs={'class':'form-control'}),
            'Carriedby':forms.TextInput(attrs={'class':'form-control'}),
            'Diesel':forms.TextInput(attrs={'class':'form-control'}),
            'Price':forms.NumberInput(attrs={'class':'form-control'}),
            'Status':forms.TextInput(attrs={'class':'form-control'}),
            
        }
