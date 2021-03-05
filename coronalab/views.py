from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.http import JsonResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

from django.db.models import Sum
# Create your views here.
from .models import * 
from .forms import TestForm1 , TestForm2, CreateUserForm, Profile
from .decorators import unauthenticated_user, allowed_users, admin_only

@unauthenticated_user
def RegisterPage(request):

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            
            group = Group.objects.get(name='reg_user')
            user.groups.add(group)
            
            RegUser.objects.create(
                user=user,
                name=user.username,
                email= user.email,
            )
            
            messages.success(request, 'Account was created for ' + username)

            return redirect('login')

    context = {'form': form}
    return render (request,'coronalab/register.html',context)


@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('adminuser')
        else:
            messages.info(request, 'Username OR password is incorrect')

    return render(request,'coronalab/login.html')


def logoutUser(request):
    logout(request)
    return redirect('login')



@login_required(login_url='login')
@admin_only
def adminuser (request):
    users = RegUser.objects.all()
    tests = Test.objects.all()
    total_test = tests.count()
    positive = tests.filter(status='positive').count()
    negative = tests.filter(status='negative').count()
    context = {'users': users, 'tests':tests,
                'total_test':total_test, 'positive':positive,
                'negative':negative}
    return render(request,'coronalab/adminuser.html',context)



@login_required(login_url='login')
def Testcenter(request):
    testcenter = TestCenter.objects.all()
    context = {'testcenter': testcenter}
    return render(request,'coronalab/testcenter.html',context)



@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def reg_user(request,pk_user):
    user = RegUser.objects.get(id=pk_user)
    tests = user.test_set.all()
    test_count = tests.count()
    
    context = {
        'user':user, 'tests':tests,'test_count':test_count,
    }
    return render(request,'coronalab/user.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateRequest(request,pk):
    test = Test.objects.get(id=pk)
    form = TestForm1(instance=test)
    if request.method == 'POST':
        form = TestForm1(request.POST, instance=test)
        if form.is_valid():
            form.save()
            return redirect('adminuser')
            
        
    context={'form':form}
    return render(request,'coronalab/request_form.html',context)



@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteRequest(request,pk):
    test = Test.objects.get(id=pk)
    if request.method == 'POST':
        print(test)
        test.delete()
        return redirect('adminuser')

    context= {'user':test}
    return render(request,'coronalab/delete.html',context)




@login_required(login_url='login')
@allowed_users(allowed_roles=['reg_user'])
def requestTest(request,pk):
    user = RegUser.objects.get(id=pk)
    form = TestForm2(initial={'user': user})
    if request.method == 'POST':
        form = TestForm2(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user-page')
            
    context = {'form':form}
    return render(request,'coronalab/request_form.html',context)



@login_required(login_url='login')
@allowed_users(allowed_roles=['reg_user'])
def userPage(request):
    username = request.user.username
    user = RegUser.objects.get(name=username)
    tests = user.test_set.all()
    test_count = tests.count()
    context = {'tests':tests, 'user':user, 'test_count':test_count }
    return render(request, 'coronalab/user2.html',context)



@login_required(login_url='login')
@allowed_users(allowed_roles=['reg_user'])
def updateProfile(request,pk):
    user = RegUser.objects.get(id=pk)
    form = Profile(instance=user)
    if request.method == 'POST':
        form = Profile(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user-page')
            
        
    context={'form':form}
    return render(request,'coronalab/request_form.html',context)



def home(request):
    worldupdate = WorldUpdate.objects.all()
    total_pos = worldupdate.aggregate(Sum('dailypositive'))
    total_rec = worldupdate.aggregate(Sum('dailyrecoverd'))
    total_death = worldupdate.aggregate(Sum('dailydeath'))
    
    bdupdate = BangladeshUpdate.objects.all()
    bd_pos = bdupdate.aggregate(Sum('dailypositive'))
    bd_rec = bdupdate.aggregate(Sum('dailyrecoverd'))
    bd_death = bdupdate.aggregate(Sum('dailydeath'))

    context ={'total_pos': total_pos, 'total_rec': total_rec, 'total_death': total_death,
                'bd_pos':bd_pos,'bd_rec':bd_rec,'bd_death':bd_death}
    return render(request,'coronalab/home.html',context)



def worldStatus(request):
    worlddate = []
    worlddata = []
    worldupdate = WorldUpdate.objects.all()
    for i in worldupdate:
        worlddate.append(i.date)
        worlddata.append(i.dailypositive)

    data = {'worlddate':worlddate ,
                'worlddata': worlddata}
    return JsonResponse(data)



def worldTotalStatus(request):
    worlddate = []
    worlddata = []
    worldupdate = WorldUpdate.objects.all()
    for i in worldupdate:
        worlddate.append(i.date)
        worlddata.append(i.dailytotaltest)

    data = {'worlddate':worlddate ,
                'worlddata': worlddata}
    return JsonResponse(data)


def worldRecoveredStatus(request):
    worlddate = []
    worlddata = []
    worldupdate = WorldUpdate.objects.all()
    for i in worldupdate:
        worlddate.append(i.date)
        worlddata.append(i.dailyrecoverd)

    data = {'worlddate':worlddate ,
                'worlddata': worlddata}
    return JsonResponse(data)


def worldDeathStatus(request):
    worlddate = []
    worlddata = []
    worldupdate = WorldUpdate.objects.all()
    for i in worldupdate:
        worlddate.append(i.date)
        worlddata.append(i.dailydeath)
    data = {'worlddate':worlddate ,
                'worlddata': worlddata}
    return JsonResponse(data)


def bangladeshStatus(request):
    bddate = []
    bdposdata = []
    bdupdate = BangladeshUpdate.objects.all()
    for i in bdupdate:
        bddate.append(i.date)
        bdposdata.append(i.dailypositive)
        
    data = {'bddate':bddate ,
                'bdposdata': bdposdata}
    return JsonResponse(data)


def bangladeshRecStatus(request):
    bddate = []
    bdrecdata = []
    bdupdate = BangladeshUpdate.objects.all()
    for i in bdupdate:
        bddate.append(i.date)
        bdrecdata.append(i.dailyrecoverd)
        
    data = {'bddate':bddate ,
                'bdrecdata': bdrecdata}
    return JsonResponse(data)


def bangladeshDeathStatus(request):
    bddate = []
    bddeathdata = []
    bdupdate = BangladeshUpdate.objects.all()
    for i in bdupdate:
        bddate.append(i.date)
        bddeathdata.append(i.dailydeath)
        
    data = {'bddate':bddate ,
                'bddeathdata': bddeathdata}
    return JsonResponse(data)


