from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, NewProjectForm, ProfileForm
from .models import  Projects, Profile
from .serializer import ProjectSerializer
from .permissions import IsAdminOrReadOnly
from django.contrib.auth.models import User
from .serializer import ProjectSerializer, ProfileSerializer

# Create your views here.
class ProjectList(APIView):
    
    def get(self, request, format=None):
        all_projects = Projects.objects.all()
        serializers = ProjectSerializer(all_projects, many=True)
        return Response(serializers.data)
    
    def post(self, request, format=None):
        serializers.ProjectSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
   
    permission_classes = (IsAdminOrReadOnly,)

class ProjectDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_project(self, pk):
        try:
            return Projects.objects.get(pk=pk)
        except Projects.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        project = self.get_project(pk)
        serializers = ProjectSerializer(project)
        return Response(serializers.data)
    
    def put(self, request, pk, format=None):
        project = self.get_project(pk)
        serializers = ProjectSerializer(project, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        project = self.get_project(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProfileList(APIView):
    
    def get(self, request, format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)

def api(request):
    
    return render(request, 'api.html')

@login_required(login_url='/login')
def index(request):
    current_user = request.user
    projects = Projects.get_projects()
    return render(request, 'index.html', {'current_user':current_user, 'projects':projects})

def signup(request):
    name = 'Signup'
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form, 'name':name})

@login_required(login_url='/login/')
def new_project(request):
    current_user = request.user
   
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user= current_user
            project.save()
        return redirect('home')
    else:
        form = NewProjectForm()
    return render(request, 'new_project.html', {'current_user':current_user, 'form':form})

def profile(request):
    current_user = request.user

    projects = Projects.get_projects()
    
    return render(request, 'profile.html', {'current_user':current_user, 'projects':projects})

@login_required(login_url='/login/')
def update_profile(request):
    current_user = request.user
    profile = Profile(user=request.user)
   
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES,  instance=request.user.profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user= current_user
            profile.save()
        return redirect('home')
    else:
        form = ProfileForm(instance=request.user.profile)
        args = {}
        args['form'] = form
    return render(request, 'update_profile.html', {'current_user':current_user, 'form':form})

def search_project(request):
    """
    Function that searches for projects
    """
    if 'username' in request.GET and request.GET["username"]:
        search_term = request.GET.get("username")
        searched_profiles = User.objects.filter(username__icontains=search_term)
        message = f"{search_term}"
        profiles = User.objects.all()
        
        return render(request, 'search.html', {"message": message, "usernames": searched_profiles, "profiles": profiles, })

    else:
        message = ", no project/user by that name"
        return render(request, 'search.html', {"message": message})


