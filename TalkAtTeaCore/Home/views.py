from django.shortcuts import render, redirect
from django.contrib.auth.models import *
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.http import JsonResponse
from django.core.serializers import serialize
import json

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
        
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return render(request, "dashboard.html")
        else:
            context = {'error_message': "Invalid Credentials"}
            request.session['dashboard_login_error_message'] = context
        
            return redirect('view_admin_dashboard')
    
    else:
        if request.user.is_authenticated:
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
    
def save_admin_user_details(request):

    if request.user.is_authenticated:
        current_user_id = request.user.id

        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        primary_mobile_number = request.POST.get('primaryMobileNumber')
        alternate_mobile_number = request.POST.get('alternateMobileNumber')
        user_address = request.POST.get('userAddress')
        user_city = request.POST.get('userCity')
        user_country = request.POST.get('userCountry')
        user_postal_code = request.POST.get('userPostalCode')
        user_bio = request.POST.get('userBio')

        try:
            user = User.objects.get(id = current_user_id)
            user.first_name = first_name
            user.last_name = last_name
            user.save()

            admin_user_profile = UserProfile.objects.filter(user_id = current_user_id)

            if len(admin_user_profile) == 0:
                profile = UserProfile.objects.create(user_id = current_user_id)

            admin_user_details = UserProfile.objects.get(user_id = current_user_id)
            admin_user_details.address = user_address
            admin_user_details.primary_mobile_number = primary_mobile_number
            admin_user_details.alternate_mobile_number = alternate_mobile_number
            admin_user_details.city = user_city
            admin_user_details.country = user_country
            admin_user_details.postal_code = user_postal_code
            admin_user_details.bio = user_bio

            admin_user_details.save()

        except:
            return redirect('userProfile')

        return redirect('userProfile')
    
    else:
        return redirect('view_admin_dashboard')
    
def save_admin_user_password(request):

    if request.user.is_authenticated:

        current_user_id = request.user.id
        new_password = request.POST.get("newPassword")

        try:
            user = User.objects.get(id = current_user_id)
            user.set_password(new_password)
            user.save()
        except:
            return redirect('userProfile')
        
        context = {'error_message': "After Password Change please Log-in again to continue."}
        request.session['dashboard_login_error_message'] = context

        return redirect('view_admin_dashboard')

    else:
        return redirect('view_admin_dashboard')
    
def show_all_user_profiles(request):

    if request.user.is_authenticated:
        userDetails = User.objects.all().order_by('-pk')
        context = {'userDetails' : userDetails}

        return render(request, 'allUserProfiles.html', context = context)

    else:
        return redirect('view_admin_dashboard')

def get_user_details_with_id(request, user_id):

    if request.user.is_authenticated:

        try:
            user_details = User.objects.get(id = user_id)
            user_profile_details = UserProfile.objects.get(user_id = user_id)

            serialized_user_Details = serialize('json', [user_details])
            serialized_user_profile_details= serialize('json', [user_profile_details])

            data = {
                'userDetails': serialized_user_Details,
                'userProfileDetails': serialized_user_profile_details
                }

            return JsonResponse(data, status = 200, safe = False)
        except Exception as error:
            data = {
                'error_message': 'Error in fetching data.'
                }

            return JsonResponse(data, status = 500)
    
    else:
        data = {
            'error_message': 'You are not authenticated to access this data.'
            }
        return JsonResponse(data, status = 401)

def create_new_user(request):

    if request.user.is_authenticated:
        if request.method == 'POST':

            try:
                post_data = json.loads(request.body)
                
                firstName = post_data.get('firstName')
                lastName = post_data.get('lastName')
                mobile = post_data.get('mobile')
                email = post_data.get('email')
                address = post_data.get('address')
                city = post_data.get('city')
                country = post_data.get('country')
                username = post_data.get('username')
                password = post_data.get('password')
                is_super_user = post_data.get('isSuperUser')

                print(firstName, lastName, mobile, email, address, city, country, username, password, is_super_user)
                if(User.objects.filter(username = username).exists()):
                    data = {"message": "Username \"" + username + "\" already exists. Please provide a different username.",
                            'hasError': True
                            }
                    return JsonResponse(data)
                if(User.objects.filter(email = email).exists()):
                    data = {"message": "Email \"" + email + "\" already exists. Please provide a different Email.",
                            'hasError': True
                            }
                    return JsonResponse(data)
                
                user = User.objects.create_user(first_name = firstName, last_name = lastName, username = username, password = password, email = email, is_superuser = is_super_user)
                user.save()
                print("Done till here..")

                profile = UserProfile.objects.create(user_id = user.pk)
                user_profile_details = UserProfile.objects.get(user_id = user.pk)
                user_profile_details.primary_mobile_number = mobile
                user_profile_details.address = address
                user_profile_details.city = city
                user_profile_details.country = country
                user_profile_details.save()

                data = {"message": "User Created", "hasErrors": False}
                return JsonResponse(data)
            
            except Exception as error:
                data = {"message": error,
                            'hasError': True
                            }
                return JsonResponse(data)
        else:
            data = {"message": "fail"}
            return JsonResponse(data)
    else:
        data = {"message": "fail"}
        return JsonResponse(data)
