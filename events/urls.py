
from django.urls import path
from .import views
urlpatterns = [

    # path('',views.home,name='home')
        path('',views.home,name='home'),
        path('search_anything/',views.search_anything,name='search'),
        path('login_user/',views.login_user,name='login'),
        path('logout_user/',views.logout_user,name='logout'),

    
]
