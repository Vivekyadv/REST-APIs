from django.shortcuts import render
from django.http import JsonResponse

# third party imports
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import PostSerializer
from .models import Post 


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
		qs = Post.objects.all()
		serializer = PostSerializer(qs, many=True)
		return Response(serializer.data)

	# to handle post request (data from user)
	def post(self, request, *args, **kwargs):
		# pass user data (request.data) to PostSerializer
		serializer = PostSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors)