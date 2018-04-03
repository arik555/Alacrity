from django.urls import path, include
from .views import user_registry, group_registry, registration_data
urlpatterns = [
    path('user/', user_registry, name='u_register'),
    path('team/', group_registry, name='g_register'),
    path('data/', registration_data, name='reg_data'),
    # path('display-teams/', show_groups, name='display_teams'),
]