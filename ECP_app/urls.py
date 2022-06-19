from django.urls import include
from django.urls import re_path 
from . import views
urlpatterns = [
	re_path('',views.homepage,name='home'),
	re_path('colleges/',views.college_list,name='colleges'),
	re_path('college/<str:pk>/',views.college_branch,name='college_branch'),
	re_path('college/<str:pk1>/<str:pk2>',views.college_branch_student,name='cbs'),
]