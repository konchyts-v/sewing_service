from django import forms

class QuestionForm(forms.Form):
	title = forms.CharField(max_length=100)
	body = forms.CharField(widget=forms.Textarea)
	sender = forms.EmailField()