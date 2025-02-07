from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
  path('', IndexView.as_view(), name='index'),
  path('worker-sign-up', WorkerSignUpView.as_view(), name='worker-sign-up'),
  path('worker-sign-in', WorkerSignInView.as_view(), name='worker-sign-in'),
  path('worker-menu', WorkerMenuView.as_view(), name='worker-menu'),
  path('worker-add-order', WorkerAddOrderView.as_view(), name='worker-add-order'),
  path('worker-add-client', WorkerAddClientView.as_view(), name='worker-add-client'),
  path('order-entries', WorkerEntriesView.as_view(), name='order-entries'),
  path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
