from django.urls import path
from . import views

app_name = "base"

urlpatterns = [
    path("login/", views.login_page, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.register_user, name="register"),
    path("profile/<str:pk>/", views.profile_user, name="profile"),
    path("", views.home, name="home"),
    path("room/<str:pk>/", views.room, name="room"),
    path("create-room/", views.create_room, name="create-room"),
    path("update-room/<str:pk>", views.update_room, name="update-room"),
    path("delete-room/<str:pk>", views.delete_room, name="delete-room"),
    path("delete-message/<str:pk>", views.delete_message, name="delete-message"),
    path("update-user/", views.update_user, name="update-user"),
    path("topics/", views.topics_page, name="topics"),
    path("activity/", views.activity_page, name="activity"),
]
