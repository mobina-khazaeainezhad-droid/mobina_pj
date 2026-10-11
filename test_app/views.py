from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from test_app.models import Contact
from test_app.forms import NameForm ,ContactForm,NewsletterForm



def index_view(request):
    return render(request, 'test_app/index.html')

def about_view(request):
    return render(request, 'test_app/about.html')

def contact_view(request):
    if request .method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    form = ContactForm()        
    return render(request, 'test_app/contact.html',{'form':form})

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
            

def test2_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('done')
        else:
            return HttpResponse('not valid')
        
    form = ContactForm()   
    return render(request, 'test_app/test2.html',{'form':form})



