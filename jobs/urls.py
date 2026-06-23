
from django.urls import path
from . import views

app_name = 'jobs'
# all the url patterns 
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:job_id>/", views.detail, name="detail"),
    path("new/", views.new, name="new"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
    path("profile", views.profile, name="profile"),

]