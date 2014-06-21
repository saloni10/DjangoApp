from django.shortcuts import render
from student.models import *
from student.form import Sform


                
def fee(request):
    error = False
    form = Sform()
    if 'Roll_no' in request.GET:
       q = request.GET['Roll_no']
       if not q:
            error = True
       else:
            val = Student.objects.filter(roll_no=q)
            return render(request, 'fee.html', {'list': val, 'query': q})
 
    
    return render(request, 'form.html',{'error':error,'form':form})    


def form(request):
    form = Sform()
    return render(request,'form.html',{'form':form})
