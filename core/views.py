from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from anitabregister.models import Members

def home(request):
    members=Members.objects.count()
    data={"anitabregister":members,}
    return render(request,"home.html",data)
# Create your views here.
