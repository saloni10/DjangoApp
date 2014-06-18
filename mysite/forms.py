from django import forms
from student.models import Student
class ContactForm(forms.Form):
    
    subject=forms.CharField()
    email=forms.EmailField(required=False)
    message=forms.CharField(widget=forms.Textarea)

class FeeForm(forms.Form):
    roll_no = forms.IntegerField()
