from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import input,update_form
from .models import note
from django.contrib.auth.models import User

# Create your views here.
data = note.objects.all()


def home(request):
    if request.method == 'POST':
        form = input(request.POST)
        if form.is_valid():
            form.save(current_user=request.user)
            
           
    else:
        form = input()

    if request.user.is_authenticated:
        user = request.user
        user = user.user_notes.all()
    else:
        user = None

    context = {'form':form,'current_data':user }

        
    return render(request,'ht_files/homepage.html',context)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request,'ht_files/register.html',context)

def note_detail(request, id):
    global nt_ob
    nt_ob = note.objects.get(id=id)
    if request.method == 'POST':
        form = update_form(request.POST,instance=nt_ob)
        if form.is_valid():
            form.save()
            
    else:
        form = update_form(instance=nt_ob)

    
    context_window = {'note_data':nt_ob,'form':form}

    return render(request,'ht_files/detail.html',context_window)

def delete(request):

    del_it = nt_ob 
    del_it.delete()

    return redirect("home")

    #return render(request,'ht_files/delete.html')