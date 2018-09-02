from django.test import TestCase
from django.shortcuts import render

# Create your tests here.
def test(request):
	return render(request,'test.html')
