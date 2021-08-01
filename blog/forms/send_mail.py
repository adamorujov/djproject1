from django import forms

class MailForm(forms.Form):
    receiver = forms.EmailField(label='Email', max_length=100)
    subject = forms.CharField(label='Subject', max_length=200)
    mail = forms.CharField(label='Mail', widget=forms.Textarea())
