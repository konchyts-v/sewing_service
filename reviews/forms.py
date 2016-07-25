from django import forms

class Reviews_Form(forms.Form):
	sender_name = forms.CharField(max_length=20)
	message = forms.CharField(widget=forms.Textarea)