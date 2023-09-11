from django.shortcuts import render ,redirect
from django.contrib.auth.models  import User
from .models import Profile
from .forms import Login_Form ,Update_user_form,Creat_user_form
from django.contrib.auth import authenticate ,login
from django.contrib.auth.decorators import login_required
# Create your views here.



def doctor_list(request):
    doctors_objects = User.objects.all()
    context = {
        'doctorsview':doctors_objects
    }
    return render(request , 'user/doctor_list.html',context)




def doctor_detail_function(request  ,doctorslug):
    doctors_objects = Profile.objects.get(slug = doctorslug)
    context = {
        'doctor_detail_view':doctors_objects
    }
    return render(request , 'user/doctor_detail.html',context)





def login_user(request):
    if request.method == 'POST':
        form = Login_Form()
        username_var = request.POST['username']
        password_var = request.POST['password']
        user  =authenticate(request , username = username_var ,password = password_var)
         # authenticate to get data of user 
        if user is not None:
            login(request , user)
            return redirect('accounts:doctor_list') # to get url of accounts then the url od doctorlist page
    else:
            form = Login_Form() 
            
    return render(request , 'user/login.html',{
        'form':form
    })
    
    
    
    
    
    
# @login_required(login_url='accounts:login') # when user is not logined yet it will not can open myprofile page it should be go to login page first 
# # this line will go automatic to loign page when he trying to open myprofile page without login

# cuz i will need it in many apps i will put loginurl in settings.py 
@login_required()
def myprofile(request):
    return render(request , 'user/myprofile.html',{})






def update_profile(request): # update user data 
    userform = Update_user_form(instance=request.user)
    
    if request.method == 'POST':
         userform = Update_user_form(request.POST,instance=request.user)
    if userform.is_valid():
        userform.save()
        return redirect('accounts:doctor_list')
    return render(request , 'user/update_profile.html',{
        'user_form_data':userform
    })





def signup(request):
    if request.method == 'POST':
        signup_form = Creat_user_form(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            
            # here this code will open login  automatic after signup and will open doctor list page
            username = signup_form.cleaned_data.get('username')  
            password = signup_form.cleaned_data.get('passeord')    
            user  =authenticate(  username = username ,password = password)
            login(request , user)
            return redirect('accounts:doctor_list')
        
    else:
        signup_form = Creat_user_form()
            
    return render(request , 'user/signup.html',{
        'signupform':signup_form
    })