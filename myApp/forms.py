from django import forms

class EmployeeForm(forms.Form):
	eid=forms.IntegerField()
	ename=forms.CharField()
	ephnno=forms.IntegerField()
	email=forms.CharField()
	sal=forms.FloatField()