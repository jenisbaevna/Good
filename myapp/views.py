from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def uy(request):
    numbers=[343,65,9870,123,122]
    misali={
        'sanlar':numbers
    }
    return render(request,template_name='home.html',context=misali)
def haqqi(request):
    return render(request,template_name='about.html')
def atifamiliyasi(request,name,surname):
    magliwmatlar={
        'ati':name,
        'familiyasi':surname
    }
    return render(request,template_name='misali.html',context=magliwmatlar)

def acules(request,a,b):
    natiyje=int(a)+int(b)
    return HttpResponse(f'Natiyje:{natiyje}')