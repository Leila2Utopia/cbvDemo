from django.shortcuts import render,HttpResponse
from django.views import View

class Pview(View):
    name='lary'
    def get(self,request):
        return HttpResponse(self.name)

class Sview(View):
    name='lily'

# Create your views here.
def my_view(request):
    if request.method=='GET':
        return HttpResponse('OK')


class MyView(View):
    def get(self,request):
        return HttpResponse('OK')


