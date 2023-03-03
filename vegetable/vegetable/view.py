


from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect, render 
from service.models import Services
from django.core.paginator import Paginator

from .form import GeeksForm


   


def get_post(request):
    result=0
    dic={}
    try:
        if request.method=='POST':
            n1=int(request.POST.get('num1'))
            n2=int(request.POST.get('num2'))
            result=n1+n2
            dic={"n_1":n1,
                  "n_2":n2,
                  "results":result
                   }
            url="/about/? output={}.format{result}"
        #n1=int(request.GET('num1'))
        #n2=int(request.GET('num2'))
        return HttpResponseRedirect('/about/',url)

        
    except:
        pass
    return render(request,"form.html",dic)

    
    


def page(request):
    return render (request,"index.html")
def menu(request):
    return render (request,"menu.html")
def sumbitform(request):
    n=GeeksForm
    result=0
    dic ={'n_6':n}
    try:
        if request.method=='POST':
            n1=int(request.POST.get('num1'))
            n2=int(request.POST.get('num2'))
            result=n1+n2
            dic={"n_1":n1,
                  "n_2":n2,
                  "results":result,
                  "n_6":n
                   }
            url="/about/? output={}.format{result}"
        #n1=int(request.GET('num1'))
        #n2=int(request.GET('num2'))
    
    except:
        pass
    return render(request,"form.html",dic)
    
def about(request):
    if request.method=="GET":
        output=request.GET.get('output')
        
    return render (request,"about.html",{"output":output})
def dish(request):
    return render (request,"dish.html")
def even(request):
    c=''
    n=0
    if request.method=="POST":
        n=int(request.POST.get('number'))
    if n%2==0:
        c="even"
    else:
        c="odd"
    return render(request,"even.html",{"c":c})
    
def dynmic_page(request):
    
    fruits= Services.objects.all()
    datas={
        "std":fruits
    }   
    return render(request,"index.html",datas)

  