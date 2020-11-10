from django.shortcuts import render, HttpResponseRedirect,redirect
from .models import DataForm
from .forms import formdata
# Create your views here.
def home(request):
    if request.method == 'POST':
        form=formdata(request.POST)
        if form.is_valid():
            dt=form.cleaned_data['Date']
            soc=form.cleaned_data['Sizeofcontainer']
            fm=form.cleaned_data['From']
            to=form.cleaned_data['To']
            ctm=form.cleaned_data['Customer']
            cdb=form.cleaned_data['Carriedby']
            dsl=form.cleaned_data['Diesel']
            Prc=form.cleaned_data['Price']
            sts=form.cleaned_data['Status']
            reg=DataForm(Date=dt,Sizeofcontainer=soc,From=fm,To=to,Customer=ctm,Carriedby=cdb,Diesel=dsl,Price=Prc,Status=sts)
            reg.save()
           
    else:
        form=formdata()
    return render(request, 'myapplication/home.html', {'form':form})

def show(request):
    record=DataForm.objects.all()
    return render(request, 'myapplication/show.html',{'records':record})


def update(request,id):
    if request.method == 'POST':
        pi=DataForm.objects.get(pk=id)
        form=formdata(request.POST, instance=pi)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/show/')
    else:
          pi=DataForm.objects.get(pk=id)
          form=formdata(instance=pi)
    return render(request,'myapplication/update.html', {'form':form})



def delete(request,id):
    if request.method == 'POST':
        pi=DataForm.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/show/')
        
    
   