from django.http import HttpResponse
from django.template import loader
from .models import Member

def djangoapp(request):
    djangoapp = Member.objects.all().values() # get all the members
    template = loader.get_template('members.html') # load the template
    context = { # context is a dictionary that maps template variable names to Python objects
        'djangoapp': djangoapp,
    }
    return HttpResponse(template.render(context, request))

def memberdetails(request, id):
    mymember = Member.objects.get(id=id) # get the member with the given id
    template = loader.get_template('memberdetails.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())