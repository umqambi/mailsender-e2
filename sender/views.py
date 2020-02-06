from django.shortcuts import render, redirect
from django.http.response import HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy

from .models import MailForSend
from .forms import MailForm 


class Index(CreateView):  
    model = MailForSend  
    form_class = MailForm  
    success_url = reverse_lazy('mails')  
    template_name = 'index.html'  

def Mails(request):
    template = loader.get_template('mails.html')
    mails = MailForSend.objects.all().order_by("-pk")[:10]
    mails_list = {
        "mails": mails,
    }
    return HttpResponse(template.render(mails_list, request))