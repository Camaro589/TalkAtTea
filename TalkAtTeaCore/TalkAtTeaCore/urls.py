"""
URL configuration for TalkAtTeaCore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Home.views import *

urlpatterns = [
    path('adminLogin/', admin.site.urls),
    path('', view_home, name = "view_home"),
    path('admin/', view_admin_dashboard, name = "view_admin_dashboard"),
    path('dashboard/', dashboard, name = "dashboard"),
    path('userProfile/', user_profile, name = "userProfile"),
    path('saveAdminUserDetails/', save_admin_user_details, name = "saveAdminUserDetails"),
    path('saveAdminUserPassword/', save_admin_user_password, name = "saveAdminUserPassword"),
    path('showAllUserProfiles/', show_all_user_profiles, name = "showAllUserProfiles"),
    path('getUserDetails/<int:user_id>', get_user_details_with_id, name = "getUserDetails"),
    path('createNewUser', create_new_user, name = "createNewUser"),
    path('deleteUser/<int:user_id>', delete_user, name = "deleteUser"),
    path('showAllRestaurants/', show_all_restaurants, name = "showAllRestaurants"),
    path('showAllRestaurants/restaurantDetails/<int:restaurant_id>', specific_restaurant_details, name = "restaurantDetails"),
    path('createNewRestaurant', create_new_restaurant, name = "createNewRestaurant"),
]