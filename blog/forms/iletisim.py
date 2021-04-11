from django import forms
from blog.models import IletisimModel

class IletisimForm(forms.Form):
    email = forms.EmailField(max_length=100, label='Email', widget=forms.TextInput(attrs={
        'class' : 'form-control border border-secondary',
        'id' : 'exampleInputEmail1',
        'aria-describedby' : 'emailHelp',
    }))
    isim_soyisim = forms.CharField(max_length=50, label='Isim Soyisim', widget=forms.TextInput(attrs={
        'class' : 'form-control border border-secondary',
        'id' : 'exampleInputName1',
    }))
    mesaj = forms.CharField(label='Mesaj', widget=forms.Textarea(attrs={
        'class' : 'form-control border border-secondary',
        'id' : 'exampleInputMessage1',
        'style' : 'resize:none;',
        'rows' : 1,
    }),)

class IletisimForm1(forms.ModelForm):
    class Meta:
        model = IletisimModel
        fields = ('isim_soyisim', 'email', 'mesaj')
        widgets = {
            'isim_soyisim' : forms.TextInput(attrs={
                'class' : 'form-control border border-secondary',
                'id' : 'exampleInputName1',
                'placeholder' : 'Isim Soyisim',
            }),
            'email' : forms.EmailInput(attrs={
                'class' : 'form-control border border-secondary',
                'id' : 'exampleInputEmail1',
                'aria-describedby' : 'emailHelp',
                'placeholder' : 'Email',
            }),
            'mesaj' : forms.Textarea(attrs={
                'class' : 'form-control border border-secondary',
                'id' : 'exampleInputMessage1',
                'style' : 'resize:none;',
                'placeholder' : 'Mesaj',
            }),
        }

