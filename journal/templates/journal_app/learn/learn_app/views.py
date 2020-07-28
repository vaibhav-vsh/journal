from django.shortcuts import render
from django.http import HttpResponse
from learn_app.models import Kid,Student
from learn_app.forms import EmpForm,UserForm,UserProfileForm

# Create your views here.

def index(request):
    return HttpResponse("This is the views.py file in the learn_app! Base func!")

def index1(request):
    return HttpResponse("This is the views.py file in the learn_app! Index1 func!")

def index2(request):
    return HttpResponse("This is the views.py file in the learn_app! Index2 func!")

def temps(request):
    my_dict={
    'print_me':'This is coming from views.py via template tag!',
    'and_me':'This is also coming from views.py via template tag! Second key!'
    }
    return render(request,'learn_app/index.html',context=my_dict)

def temps2(request):
    return render(request,'learn_app/index2.html')

def data(request):
    kid_list=Kid.objects.all()
    stu_list=Student.objects.all()
    sch_dict={'kids':kid_list,'stu':stu_list}
    return render(request,'learn_app/data.html',context=sch_dict)

def emp_form(request):
    form=EmpForm()
    if request.method=='POST':
        form=EmpForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponse('Your data has been saved!')
        else:
            print("Error! Form invalid!")

    return render(request,'learn_app/form.html',{'form_key':form})

def register(request):
    registered=False
    if request.method=='POST':
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user

            if 'pic' in request.FILES:
                profile.pic=request.FILES['pic']
            profile.save()

            registered=True

        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form=UserForm()
        profile_form=UserProfileForm()

    return render(request,'learn_app/registration.html',{
    'user_form':user_form,
    'profile_form':profile_form,
    'registered':registered
    })
