from rest_framework import serializers
from .models import Post

# # This is how django form works
# from django import forms
# class djangoPostForm(forms.ModelForm):
# 	class meta:
# 		model = post
# 		fields = (
# 		'title', 'description'
# 		)

class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = (
			'title', 'description', 'owner', 'timestamp'
		)
