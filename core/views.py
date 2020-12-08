from django.shortcuts import render
from django.http import JsonResponse

def view(request):
	data = {
		'title': 'hello',
		'description': 'desc one'
	}

	return JsonResponse(data)
