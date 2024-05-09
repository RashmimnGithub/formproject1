from django.shortcuts import render
from myApp.forms import EmployeeForm

# Create your views here.
def formView(request):
	f=EmployeeForm()
	if request.method=="POST":
		f=EmployeeForm(request.POST)
		if f.is_valid():
			eid=f.cleaned_data["eid"]
			ename=f.cleaned_data["ename"]
			ephnno=f.cleaned_data["ephnno"]
			email=f.cleaned_data["email"]
			sal=f.cleaned_data["sal"]
			d={'eid':eid,'name':ename,'phn':ephnno,'email':email,'sal':sal}
			return render(request,'myApp/output.html',d)
	d={'form':f}
	return render(request,'myApp/input.html',d)