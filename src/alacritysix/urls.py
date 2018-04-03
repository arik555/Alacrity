"""alacritysix URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from registration.views import add_event, show_events, index_page, ala_index_page, del_user, del_grp, del_eve
from accounts.views import logout_user

urlpatterns = [
    path('', index_page, name='index'),
    path('admin/', admin.site.urls),
    path('main_page/', ala_index_page, name="alacrity_index"),
    path('registry/', include('registration.urls')),
    path('add_event/', add_event, name="add_event"),
    path('show_events/', show_events, name="my_events"),
    path('auth/', include('accounts.urls')),
    path('logout/', logout_user, name="logout"),
    path('delete-user/<int:id>/', del_user, name="usr_del"),
    path('delete-group/<int:id>/', del_grp, name="grp_del"),
    path('delete-event/<int:id>/', del_eve, name="eve_del"),
]
