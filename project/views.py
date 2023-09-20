from django.shortcuts import render,redirect
from .models import inserting
# Create your views here.
def index(request):
    data = inserting.objects.all()
    return render(request, 'app/index.html',{'data':data})

def create(request):
    name = request.GET.get('name')
    number = request.GET.get('number')
    context = inserting(name=name, number=number)
    context.save()
    return redirect('/')

def delete(request,id):
    data = inserting.objects.get(pk=id)
    data.delete()
    return redirect('/')