from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [ 
    path('',views.index,name='index'),
    path('list/',views.PlaceListView.as_view(),name='place_list'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('place/<str:pk>', views.PlaceDetailView.as_view(), name='place_detail'),
    path('place/new/', views.CreatePlaceView.as_view(), name='place_new'),
    path('place/<str:pk>/add/', views.confirm_save, name='place_add'),
    path('place/<str:pk>/remove/', views.PlaceDeleteView.as_view(), name='place_remove'),
    path('place/<str:pk>/edit/', views.PlaceUpdateView.as_view(), name='place_edit'),
    path('place/<str:pk>/comment/', views.add_comment_to_place, name='add_comment_to_place'),
    path('rate/', views.rate_place, name='rate_place'),
    path('visited/', views.visited_place, name='visited_place'),
    path('recommend/', views.RecommendListView.as_view(), name='recommend'),
    path('family/', views.family, name='family'),
    path('register/', views.register, name="register"),
    path('logout/',views.logout,name='logout'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="registration/password_reset.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="camp/password_reset_confirm.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="camp/password_reset_complete.html"), name="password_reset_complete"),
]