from django.test import TestCase
from .models import Profile,Projects
import datetime as dt
from django.contrib.auth.models import User



# Create your tests here.
class ProjectTestCLass(TestCase):
    '''
    setup self instance of project
    '''
    def setUp(self):
        self.project = Projects( title='award',project_image='/static/images/log.png', caption='awards test', project_link='www.awards.com', user= '1')
    
    ''' 
    test instance of project
    '''
    def test_instance(self):
        self.assertTrue(isinstance(self.project,Projects))


    '''
    test save project
    '''

    def test_save_image(self):
        self.project.save_project()
        project = Projects.objects.all()
        self.assertTrue(len(project)>0)

class ProfileTestClass(TestCase):
    '''
    a class to test the profile instances and its methods
    '''

    # Set up method
    def setUp(self):
        self.user = User.objects.create(id=1,username='martin')
        self.profile= Profile(profile_photo='/static/images/log.png',bio='dev',user=self.user)
        self.contact = Profile(contact = 'martin5gathu')
    
    #Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))