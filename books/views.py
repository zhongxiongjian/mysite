# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.
from django.http import HttpResponse
 
def index(request):
    return render(request, 'home.html')
	
def add(request, a, b):
    c = int(a) + int(b)
    d = '%d + %d = %d' % (int(a),int(b),int(c))
    return HttpResponse(str(d))
from django.db.models import Q
from django.shortcuts import render_to_response
from models import Book
from forms import ContactForm
def search(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(title__icontains=query) |
            Q(authors__first_name__icontains=query) |
            Q(authors__last_name__icontains=query)
        )
        results = Book.objects.filter(qset).distinct()
    else:
        results = []
    return render_to_response("books/search.html", {
        "results": results,
        "query": query
    })
@csrf_exempt
def contact(request):
#    if request.method == 'POST':
#        form = ContactForm(request.POST)
#        if form.is_valid():
#            topic = form.clean ['topic']
#            message = form.clean ['message']
#            sender = form.clean .get('sender', 'noreply@example.com')
#            send_mail(
#                'Feedback from your site, topic: %s' % topic,
#                message, sender,
#                ['administrator@example.com']
#            )
#            return HttpResponseRedirect('/contact/thanks/')
#    else:
#        form = ContactForm()
    form = ContactForm()
    return render_to_response('contact.html', {'form': form})


