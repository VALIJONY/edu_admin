from django.urls import path
from .views import MainView,AdminView,LoginView,LogoutView,UqituvchiQushishView,UquvchiQushView,UquvchiKurslariView,NewGroupView,ManitoringView,OpenGroupView,RoomView

urlpatterns=[
path('',MainView.as_view(),name='main') ,
path('for_admin/',AdminView.as_view(),name='for_admin'),
path('login/',LoginView.as_view(),name='login'),
path('logout/',LogoutView.as_view(),name='logout'),
path('add_pupil/',UquvchiQushView.as_view(),name='add_pupil'),
path('add_teacher/',UqituvchiQushishView.as_view(),name='add_teacher'),
path('course_pupil/',UquvchiKurslariView.as_view(),name='course_pupil'),
path('new_group/',NewGroupView.as_view(),name='new_group'),
path('manitoring/',ManitoringView.as_view(),name='manitoring'),
path('opengroup/',OpenGroupView.as_view(),name='opengroup'),
path('room_manitoring/<xona_raqami>',RoomView.as_view(),name='room'),

]
