from django.urls import path
from appUsers.views import *

from appUsers import views

urlpatterns = [
    # path('profile/', profile, name="profile"),
    path('profile/', list_posts, name="list_posts"),
    path('new_post/', new_post, name="new_post"),
    path('all_users/', list_users, name="list_users"),
    path('register/', register, name="register"),

]