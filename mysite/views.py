from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import Template, Context
from django.template.loader import get_template 
from django.shortcuts import render
from mysite.forms import ContactForm
from django.core.mail import send_mail
import datetime
def hello(request):
  html="<html><head><title> hello </title> <style>{body : bgcolor=pink;} {p:bgcolor=blue; color:red;} </style></head> <body><p>Hello  world! This is saloni </p> </body></html>"
  return HttpResponse(html)

def current_datetime(request):
  now=datetime.datetime.now()
  html="<html><body>It is now %s.</body></html>" % now
  return HttpResponse(html)

def hours_ahead(request, offset):
    try:
      offset= int(offset)
    except:
      raise Http404()
    dt=datetime.datetime.now()+datetime.timedelta(hours=offset)
    html="<html><body> in %s hour(s), it will be %s. </body></html>" % (offset,dt)
    return HttpResponse(html)

def first(request):
  t= Template("<html><body>My name is {{name}}")
  c= Context({'name':'saloni'})
  html=t.render(c)
  return HttpResponse(html)

def sec(request):
  t= get_template('temp.html')
  c= Context({'name':'saloni', 'class':'D2CSE','list':['mom','dad'], 'I_am_smart':True, 'you':'saloni'})
  html=t.render(c)
  return HttpResponse(html)

def new(request):
  t=get_template('new.html')
  c=Context({'section':'new','name':'salonib'})
  html=t.render(c)
  return HttpResponse(html)

def base(request):
  t=get_template('base.html')
  c=Context({'name':'you'})
  html=t.render(c)
  return HttpResponse(html)

def section(request):
  t=get_template('ext1.html')
  c=Context({'name':'you'})
  html=t.render(c)
  return HttpResponse(html)

def search_form(request):
 return render(request, 'search_form.html')

def search(request):
    if 'q' in request.GET and request.GET['q']:
        message = "You searched for: %r" % request.GET['q']
    else:
        message = "You submitted an empty form."
    return HttpResponse(message)

def search1_form(request):
 return render(request, 'search1_form.html')

def search1(request):
    if 'q' in request.GET and request.GET['q']:
        message = "You searched for: %r" % request.GET['q']
    else:
        return render(request, 'search1_form.html', {'error': True} )

def search2(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            message = 'You searched for: %r' % request.GET['q']
    return render(request, 'search1_form.html',
        {'error': error})

def contact(request):
    if request.method=='POST':
	form = ContactForm(request.POST)
	if form.is_valid():
           cd = form.cleaned_data()
           sendmail(
                 cd['subject'],
                 cd['message'],
                 cd.get('email', 'no@reply.com'),['salonibaweja10@gmail.com'],
                )
	   return HttpResponseRedirect('/thanks/')
    else:
      form=ContactForm()
    return render(request,'contact_form.html',{'form':form})

def thanks(request):
   return render(request, 'thanks.html')
  
   
    
  
