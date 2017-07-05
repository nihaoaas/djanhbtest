from django.shortcuts import render

# Create your views here.
def list_test_project(request):
	return render(request,'project/list_test_project.html')