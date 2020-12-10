# third party imports
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import PostSerializer
from .models import Post 

from rest_framework import generics
from rest_framework import mixins


'''View data using gemerics. This class is similar to 
function rest_view but in customised form'''
class restapi_view(
		mixins.ListModelMixin,
		mixins.CreateModelMixin, 
		generics.GenericAPIView
	):

	serializer_class = PostSerializer
	queryset = Post.objects.all()

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)


''' View data without using rest framework
def view(request):
	data = {
		'title': 'hello',
		'description': 'desc one'
	}

	return JsonResponse(data)
End of function view'''



'''View GET and POST request (after authentication) using rest framework
class rest_view(APIView):

	# for GET or POST request, Authenticated is required
	permission_classes = (IsAuthenticated,)


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

End of class rest_view'''