from rest_framework import serializers
from .models import Projects, Profile



class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('id','project_image', 'caption', 'project_link', 'user', 'pub_date', 'design', 'usability', 'content', 'vote_submissions')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id','user', 'profile_photo', 'bio', 'contact')