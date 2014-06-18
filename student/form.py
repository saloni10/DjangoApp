from django import forms


class Sform(forms.Form):
    Roll_no = forms.IntegerField()