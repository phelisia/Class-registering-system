from django.urls import path
from .views import register_member, student_list

urlpatterns = [
path('register/',register_member,name='register_member'),
path('list/', student_list,name='student_list')

]