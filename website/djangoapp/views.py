from django.http import HttpResponse
from django.template import loader

def djangoapp(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())