"""
URL configuration for view project.

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
from django.views.generic import TemplateView

from main.views import MainView
# from view.views import StudentRegisterView, StudentResultView, StudentRegisterFormView
from view.views import MemberRegisterFormView, MemberRegisterView, MemberResultView, StudentRegisterFormView, \
    StudentRegisterView, StudentResultView, UserRegisterFormView, UserRegisterView, UserResultView, NumberInputFormView, \
    NumberInputView, NumberResultView, TextRegisterFormView, TextRegisterView, TextResultView, EventRegisterFormView, \
    EventRegisterView, EventResultView, NumRegisterFormView, NumRegisterView, NumResultView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('member/', include('member.urls')),
    path('post/', include('post.urls')),
    path('student/register/form/', StudentRegisterFormView.as_view(), name='student-register-form'),
    path('student/register/', StudentRegisterView.as_view(), name='student-register'),
    path('student/result/', StudentResultView.as_view(), name='student-result'),
    path('member/register/form/', MemberRegisterFormView.as_view(), name='member-register-form'),
    path('member/register/', MemberRegisterView.as_view(), name='member-register'),
    path('member/result/', MemberResultView.as_view(), name='member-result'),
    path('user/register/form/', UserRegisterFormView.as_view(), name='user-register-form'),
    path('user/register/', UserRegisterView.as_view(), name='user-register'),
    path('user/result/', UserResultView.as_view(), name='user-result'),
    path('number/input/form/', NumberInputFormView.as_view(), name='number-input-form'),
    path('number/input', NumberInputView.as_view(), name='number-input'),
    path('number/result/', NumberResultView.as_view(), name='number-result'),
    path('text/register/form/', TextRegisterFormView.as_view(), name='text-register-form'),
    path('text/register/', TextRegisterView.as_view(), name='text-register'),
    path('text/result/', TextResultView.as_view(), name='text-result'),
    path('event/register/form/', EventRegisterFormView.as_view(), name='event-register-form'),
    path('event/register/', EventRegisterView.as_view(), name='event-register'),
    path('event/result/', EventResultView.as_view(), name='event-result'),
    path('num/register/form/', NumRegisterFormView.as_view(), name='num-register-form'),
    path('num/register/', NumRegisterView.as_view(), name='num-register'),
    path('num/result/', NumResultView.as_view(), name='num-result'),
    path('product/', include('product.urls')),
    path('', MainView.as_view())
]













