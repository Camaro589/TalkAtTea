from django.shortcuts import render, redirect
from django.contrib.auth.models import *
from django.contrib.auth import authenticate

def view_home(request):
    return render(request, "home.html")

def view_admin_dashboard(request):

    context = request.session.pop('dashboard_login_error_message', None)

    return render(request, "dashboardLogin.html", context = context)

def dashboard(request):

    if(request.method == 'POST'):

        username = request.POST.get('Username')
        password = request.POST.get('Password')

        try:
            user = User.objects.get(username = username)
        except User.DoesNotExist:
           context = {'error_message': "Username does not exist"}
           request.session['dashboard_login_error_message'] = context
        
           return redirect('view_admin_dashboard')
        
        user = authenticate(username = username, password = password)

        if user is not None:
            return render(request, "dashboard.html")
        else:
            context = {'error_message': "Invalid Credentials"}
            request.session['dashboard_login_error_message'] = context
        
            return redirect('view_admin_dashboard')
    
    else:
        return render(request, "dashboard.html")
    
def user_profile(request):

    return render(request, "userProfile.html")