from django.urls import path

from core import views

urlpatterns = [
    path('home',views.home,name='home'),
    path('',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('add_todo', views.add_todo, name='add_todo'),
    path('signout', views.signout, name='signout'),
    path('delete_list/<int:id>', views.delete_list, name='delete_list'),
    path('update_task/<int:pk>', views.update_task, name='update_task'),
    path('search', views.search, name='search'),

]
