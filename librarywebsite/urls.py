"""
URL configuration for mblog0927 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,  reverse
from mysite import views as mv
from mytest import views as testv
from mysite.views import book_list, borrow_book, return_book

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',mv.homepage,name="homepage"),
    path('post/<slug:slug>/',mv.showpost,name="showpost"),
    path('member/', mv.member),
    path('register/', testv.register),
    path('login/', testv.login, name='login'),
    path('logout/', testv.logout_view, name='logout'),
    path('book_list/', book_list, name='book_list'),
    path('borrow/<int:book_id>/', borrow_book, name='borrow_book'),
    path('return/<int:book_id>/', return_book, name='return_book'),

]
