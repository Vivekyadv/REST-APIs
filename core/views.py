from django.shortcuts import render
from django.http import JsonResponse

# third party imports
from rest_framework.views import APIView
from rest_framework.response import Response


# view data without using rest framework
def view(request):
	data = {
		'title': 'hello',
		'description': 'desc one'
	}

	return JsonResponse(data)


# view data using rest framework
class rest_view(APIView):
	def get(self, request, *args, **kwargs):
		data2 = {
			'name': 'Anonymous',
			'age': 78
		}
		return Response(data2)