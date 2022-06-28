from .models import Members
from.forms import Members_registsration_form
from django.shortcuts import render,redirect

def register_member(request):
  if request.method=="POST":
    form=Members_registsration_form(request.POST,request.FILES)
    if form.is_valid():
      form.save()
    else:
      print(form.errors())
  else:
    form=Members_registsration_form()
  return render(request,"register_member.html",{"form":form})

def student_list(request):
  members=Members.objects.all
  return render(request,"studentlist.html",{"members",members})  

