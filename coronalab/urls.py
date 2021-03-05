from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.RegisterPage, name='registerpage'),

    path('login/',views.loginPage ,name='login'),
    
    path('logout/',views.logoutUser ,name='logout'),

    path('', views.home, name='home'),
    
    path('world-status/', views.worldStatus, name='world-status'),
    path('world-total-status/', views.worldTotalStatus, name='world-total-status'),
    path('world-recovered-status/', views.worldRecoveredStatus, name='world-recovered-status'),
    path('world-death-status/', views.worldDeathStatus, name='world-death-status'),
    

    path('bd-status/', views.bangladeshStatus, name='bd-status'),
    path('bd-recover-status/', views.bangladeshRecStatus, name='bd-recover-status'),
    path('bd-death-status/', views.bangladeshDeathStatus, name='bd-death-status'),

    path('adminuser/',views.adminuser, name='adminuser'),

    path('user/<str:pk_user>/',views.reg_user, name='user'),
    
    path('userpage/', views.userPage, name='user-page'),

    path('testcenter/',views.Testcenter,name='testcenter'),

    path('request_test/<str:pk>',views.requestTest,name='request_test'),

    path('update_request/<str:pk>',views.updateRequest,name = 'update_request'),
    
    path('update_profile/<str:pk>',views.updateProfile,name = 'update_profile'),

    path('delete_request/<str:pk>',views.deleteRequest,name = 'delete_request')
]