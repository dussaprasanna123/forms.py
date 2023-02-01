from django import forms

class student_Forms(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField(min_value=5)
    email=forms.EmailField()
    password=forms.CharField(max_length=100,widget=forms.PasswordInput)
    address=forms.CharField(max_length=1000,widget=forms.Textarea)
