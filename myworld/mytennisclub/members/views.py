from django.http import HttpResponse
from django.template import loader

from .models import Member

def members(request):
  mem=Member.objects.all()
  template = loader.get_template('allmembers.html')
  context = {
    'members': mem,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render({}, request))