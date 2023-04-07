from django.contrib import admin
from django.urls import path
from blogapp import views
urlpatterns = [

    path('home',views.home),
    path('edit/<rid>',views.edit),
    path('delete/<rid>',views.delete),
    path('udash',views.user_dashboard),
    path('dtl',views.view_html),
    path('about',views.about,name="about_page"),
    path('contact',views.contact,name="contact_page"),
    path('',views.index,name="index_page"),
    path('post',views.post,name="post_page"),
    path('cpost',views.create_post,name="create_post"),
    path('catfilter/<catopt>',views.catfilter),    
    path('actfilter/<actopt>',views.actfilter),
    path('djangoform',views.djangoform),
    path('register',views.user_register),
    path('login',views.user_login),
    path('setcookie',views.setcookies),
    path('getcookie',views.getcookies),
    path('setsession',views.setsession),
    path('getsession',views.getsession),
    path('logout',views.user_logout),
    ]
