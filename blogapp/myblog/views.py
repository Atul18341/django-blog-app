from django.shortcuts import render
from .models import blog
# Create your views here.

def blogs(request):
   
    blogs=blog.objects.all()
    return render(request,"index.html",{'blogs':blogs})
