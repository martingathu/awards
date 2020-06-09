from django.urls import path, re_path
from django.conf.urls import url, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.signup, name='signup'),
    path('home/', views.index, name='home'),
    re_path(r'^login/', LoginView.as_view(), name='login'),
    re_path(r'^logout/', LogoutView.as_view(next_page='login'), name='logout'),
    re_path(r'^newproject/', views.new_project, name='new_project'),
    re_path(r'^profile/', views.profile, name='profile'),
    re_path(r'^search/',views.search_project,name='search_project'),
    re_path(r'^updateprofile/', views.update_profile, name='update_profile'),
    url(r'^api/projects/$', views.ProjectList.as_view(), name= 'projects'),
    url(r'api/project/project-id/(?P<pk>[0-9]+)/$',views.ProjectDescription.as_view()),
    url(r'^api/profiles/$', views.ProfileList.as_view(),name='profiles'),
    re_path(r'^api/', views.api, name='api'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)