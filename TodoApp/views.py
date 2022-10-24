

from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from . form import Todoform
from . models import Todolist

#generic views imports

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView ,UpdateView
#create views via generic views


class Tasklistview(ListView):
    model= Todolist
    template_name= 'home.html'
    context_object_name= 'tasks'


class Taskdetailview(DetailView):
    model= Todolist
    template_name= 'details.html'
    context_object_name= 'tasks'


class Taskupdateview(UpdateView):
    model= Todolist
    template_name= 'update.html'
    context_object_name= 'tasks'
    fields = ('name','date','priority')

    def get_success_url(self) :
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})
        
class Taskdeleteview(DeleteView):
    model= Todolist
    context_object_name= 'tasks'
    template_name= 'delete.html'
    success_url=reverse_lazy('cbvhome')

# Create your views here.normal functional way
def home(request):
    data=Todolist.objects.all()
    return render(request,'home.html',{'tasks':data})


#add task to to do list function
def add(request):
    if request.method=='POST':
        n=request.POST.get('name','')
        d=request.POST.get('date','')
        p=request.POST.get('priority','')
        task=Todolist(name=n,date=d,priority=p)
        task.save()
        return redirect('/')
    data=Todolist.objects.all()
    return render(request,'home.html',{'tasks':data})
        

#delete task to to do list function
def update(request,id):   

    task=Todolist.objects.get(id=id)
    form=Todoform(request.POST or None,instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request,'update.html',{'form':form,'task':task})    


#update task to to do list function
def delete(request,id):
    task=Todolist.objects.get(id=id)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html',{'task':task})        