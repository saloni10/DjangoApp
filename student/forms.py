from django import forms
from student.models import Student

class FeeForm(forms.Form):
    roll_no = forms.IntegerField()
