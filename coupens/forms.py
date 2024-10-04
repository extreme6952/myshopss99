from django import forms



class CouponeForm(forms.Form):

    code = forms.CharField()