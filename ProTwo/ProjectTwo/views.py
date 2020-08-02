from django.shortcuts import render
from django.http import HttpResponse
from ProjectTwo.models import User
from ProjectTwo.forms import NewUserForm
# Create your views here.

# def index(request):
#     return render(request,'ProjectTwo2/help.html', context=help_dict)

def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'users': user_list}
    return render(request,'ProjectTwo2/users.html', context=user_dict)   

def help(request):
    help_dict = {'help_insert': 'HELP PAGE'}
    return render(request,'ProjectTwo2/help.html', context=help_dict)

def index(request):
    # help_dict = {'help_insert': 'HELP PAGE'}
    return render(request,'ProjectTwo2/index.html')

def usernew(request):
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')

    return render(request, 'ProjectTwo2/signup.html',{'form':form})