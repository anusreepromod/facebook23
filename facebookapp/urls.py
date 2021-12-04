from django.urls.conf import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    # path('sample/', views.sample1, name='sample'),
    path('login/', views.logins, name='login'),
    path('editprofile/', views.editprofile, name='editprofile'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('changepassword/', views.fnchangepassword, name='changepassword'),
    path('sample1/', views.fnsample, name='sample1'),
    path('sample2/', views.sample2, name='sample2'),
    path('sample3/', views.loadpage),
    path('del/', views.dele),
    path('logout/', views.fnlogout),
    path('delete/', views.fndelete),
    path('updatadata/', views.fnupdatadata),
    path('update/', views.fnupdate),
    path('api/', views.fnapi),
    path('postapi/', views.fnpostapi),
    path('deleteapi/', views.fndeleteapi),
    path('dashboard1/', views.fndashboard, name='dashboard1'),
    path('registration', views.fnregistration),
    path('testsample/', views.fntest, name='testsample')
]
