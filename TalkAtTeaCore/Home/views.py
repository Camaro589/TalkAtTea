from django.shortcuts import render, redirect
from django.contrib.auth.models import *
from django.contrib.auth import authenticate, login
from .models import *

def view_home(request):
    return render(request, "home.html")

def view_admin_dashboard(request):

    context = request.session.pop('dashboard_login_error_message', None)

    return render(request, "dashboardLogin.html", context = context)

def dashboard(request):

    if request.user.is_authenticated:
        if(request.method == 'POST'):

            username = request.POST.get('Username')
            password = request.POST.get('Password')

            try:
                user = User.objects.get(username = username)
            except User.DoesNotExist:
                context = {'error_message': "Username does not exist"}
                request.session['dashboard_login_error_message'] = context
            
                return redirect('view_admin_dashboard')
            
            user = authenticate(request, username = username, password = password)

            if user is not None:
                login(request, user)
                return render(request, "dashboard.html")
            else:
                context = {'error_message': "Invalid Credentials"}
                request.session['dashboard_login_error_message'] = context
            
                return redirect('view_admin_dashboard')
        
        else:
            return render(request, "dashboard.html")
        
    else:
        return redirect('view_admin_dashboard')
    
def user_profile(request):

    if request.user.is_authenticated:
        
        current_user_id = request.user.id
        try:
            user_profile = UserProfile.objects.get(user_id = current_user_id)
            context = {'user_profile': user_profile}
        except:
            context = {'user_profile' : ""}

        return render(request, "userProfile.html", context = context)
    
    else:
        return redirect('view_admin_dashboard') 