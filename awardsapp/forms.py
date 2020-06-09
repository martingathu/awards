from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Projects, Profile


class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ('email' ,'username','password1', 'password2', )

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ('title','project_image','caption','project_link')
        exclude = ['user', 'pub_date']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

# class VoteForm(ModelForm):
#     class Meta:
#         model = Projects
#         fields = ('design','usability','content')