from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Hello, Django!")

def message(request, name, age):
	output = {}
	output["name"] = name
	output["age"] = age
	output["messge"] = "hello, " + age + " years old " + name + "!"

	return JsonResponse(output)