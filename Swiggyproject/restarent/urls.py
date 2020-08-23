"""Swiggyproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from typing import List, Any

from django.contrib import admin
from django.urls import path
from restarent import views
from Swiggyproject import settings
from django.conf.urls import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurent/', views.restaurent, name='restaurent'),
    path('reg_restaurent/', views.reg_restaurent, name='reg_restaurent'),
    path('save_reg_resrtrent/', views.save_reg_resrtrent, name='save_reg_resrtrent'),
    path('show_rest',views.show_rest,name='show_rest'),
    path('pending_restarent/',views.pending_restarent,name='pending_restarent'),
    path('approve_restarent/',views.approve_restarent,name='approve_restarent'),
    path('cancel_restarent/',views.cancel_restarent,name='cancel_restarent'),
    path('app_resrt/',views.app_resrt,name='app_resrt'),
    path('can_rest/',views.can_rest,name='can_rest'),
    path('login_restarent/',views.login_restarent,name='login_restarent'),
    path('r_login_check/',views.r_login_check,name='r_login_check'),
    path('type_of_food/',views.Type_of_food.as_view(),name='type_of_food'),
    path('profile/', views.profile, name='profile'),
    path('add_profile/', views.Add_profile.as_view(), name='add_profile'),
    path('view_profile/',views.View_profile.as_view(),name='view_profile'),
    path('edit_profile/',views.Edit_profile.as_view(),name='edit_profile'),
    path('login/',views.Login.as_view(),name='login'),
    path('register_user/',views.register_user,name='register_user'),
    path('change/<int:pk>',views.Change_Profile.as_view(),name='change_profile'),
    path('add_comment_bag/',views.add_comment_bag,name='add_comment_bag'),

    path('save_cart/',views.save_cart,name='save_cart'),
    path('all_cart_items/',views.all_cart_items,name='all_cart_items'),
    path('remove_item/',views.remove_item,name='remove_item'),
    path('check_out/',views.check_out,name='check_out'),
    path('save_check_out/',views.save_check_out,name='save_check_out'),
    path('check_out_login/',views.check_out_login,name='check_out_login'),
    path('search/',views.search,name='search'),
    path('menu/',views.menu,name='menu'),
    path('blog/',views.blog,name='blog'),
    path('addcomments/', views.addcomments, name='addcomments'),
    path('save_comment/', views.save_comment, name='save_comment'),
    path('view_comments/', views.view_comments, name='view_comments'),
    path('abt_developer/',views.abt_developer,name='abt_developer')






]
